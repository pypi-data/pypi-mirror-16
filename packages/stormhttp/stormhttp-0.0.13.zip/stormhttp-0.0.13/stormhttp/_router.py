import asyncio
import re
import socket
import typing
from ._http import *
from ._endpoints import *
from ._mountable import *
from ._compress import *
from ._utils import *

# Global Variables
__all__ = [
    "Router",
    "AbstractEndPoint",
    "FileEndPoint"
]
_QVALUE_REGEX = re.compile(r'^\s?([^;]+)\s?(?:;\s?q=(\d\.\d)|;\s?level=\d+)*$')
_PREFIX_MATCH_REGEX = re.compile(r'^\{(.+)\}$')
_PREFIX_TREE_SENTINEL = '///'
_PREFIX_TREE_MATCH = '/*/'
_PREFIX_TREE_MOUNT = '/m/'


class Router:
    def __init__(self, loop: typing.Optional[asyncio.AbstractEventLoop]=None):
        self._prefix_tree = {}
        self._loop = loop if loop is not None else asyncio.get_event_loop()

    def add_endpoint(self, route: str, methods: typing.Iterable[str], endpoint: AbstractEndPoint) -> None:
        """
        Adds a single EndPoint to the prefix tree, possibly in multiple locations
        if there are multiple methods in the same route. An error is raised if there
        is already an EndPoint object at the same location in the tree.
        :param route: Route within the prefix tree.
        :param methods: List of methods to accept.
        :param endpoint: EndPoint object to add to the tree.
        :return: None
        """
        route_steps = route.split('/')[1:]
        current_node = self._prefix_tree

        for step in route_steps:
            if step == '':
                continue

            prefix_match = _PREFIX_MATCH_REGEX.match(step)
            if prefix_match is not None:
                if _PREFIX_TREE_MATCH in current_node and prefix_match.groups()[0] != current_node[_PREFIX_TREE_MATCH]:
                    raise ValueError("Route {} has more than one match point.".format(route))
                current_node[_PREFIX_TREE_MATCH] = prefix_match.groups()[0]
                continue

            if step not in current_node:
                current_node[step] = {}
            current_node = current_node[step]

            if _PREFIX_TREE_MOUNT in current_node:
                raise ValueError("Route {} is a mounted route and cannot have a sub-route.".format(route))

        if _PREFIX_TREE_MOUNT in current_node:
            raise ValueError("Route {} is a mounted route and cannot have a sub-route.".format(route))

        if _PREFIX_TREE_SENTINEL not in current_node:
            current_node[_PREFIX_TREE_SENTINEL] = {}
        current_node = current_node[_PREFIX_TREE_SENTINEL]

        for method in methods:
            if method in current_node:
                raise ValueError("Route {} {} has more than one endpoint registered.".format(method, route))
            current_node[method] = endpoint

    def add_mount(self, prefix: str, mountable: AbstractMountable) -> None:
        """
        Adds a Mountable to a prefix in the prefix tree.
        :param prefix: Prefix to mount the Mountable to.
        :param mountable: Mountable to mount.
        :return: None
        """
        route_steps = prefix.strip("/").split("/")
        current_node = self._prefix_tree

        for step in route_steps[:-1]:
            if step == "":
                continue

            if step not in current_node:
                current_node[step] = {}
            current_node = current_node[step]
            if _PREFIX_TREE_MOUNT in current_node:
                raise ValueError("Route {} is a mounted route and cannot have a sub-route.".format(prefix))

        if route_steps[-1] in current_node:
            raise ValueError("Route {} cannot be mounted to as there is already an endpoint registered.".format(prefix))

        mountable.prefix = prefix
        if route_steps[-1] == "":
            current_node[_PREFIX_TREE_MOUNT] = mountable
        else:
            current_node[route_steps[-1]] = {_PREFIX_TREE_MOUNT: mountable}

    async def route_request(self, request: HTTPRequest) -> HTTPResponse:
        """
        Routes an HTTPRequest through the prefix tree to an EndPoint.
        :param request: Request to route to an endpoint.
        :return: HTTPResponse to the request.
        """
        route_steps = parse_url_escapes(safe_decode(request.url.path)).split('/')
        current_node = self._prefix_tree

        # Route each step, check for matching info if needed.
        for step in route_steps:
            if _PREFIX_TREE_MOUNT in current_node:
                break

            if step == '':
                continue  # This ensures that trailing / also routes to same place.

            if step in current_node:
                current_node = current_node[step]
                if _PREFIX_TREE_MOUNT in current_node:
                    break
                continue

            elif _PREFIX_TREE_MATCH in current_node:
                request.match_info[current_node[_PREFIX_TREE_MATCH]] = step
                continue
            return request.decorate_response(HTTPErrorResponse(404))

        # If there's a mount here then allow the mount to handle it.
        if _PREFIX_TREE_MOUNT in current_node:
            for middleware in request.app.middlewares if request.app is not None else []:
                await middleware.on_request(request)

            # Do the processing from the Mountable
            response = await current_node[_PREFIX_TREE_MOUNT].on_request(request)

            # Apply middleware post-processing
            for middleware in request.app.middlewares if request.app is not None else []:
                await middleware.on_response(request, response)

            if request.method == "HEAD":
                request.body = ""

            return response

        # If we find a sentinel that means there's an EndPoint to examine.
        if _PREFIX_TREE_SENTINEL in current_node:
            current_node = current_node[_PREFIX_TREE_SENTINEL]

            # Allow the HEAD method as if it were a GET method.
            if request.method in current_node or (request.method == "HEAD" and "GET" in current_node):
                endpoint = current_node[request.method if request.method != "HEAD" else "GET"]
                try:
                    # Apply middleware pre-processing
                    for middleware in request.app.middlewares if request.app is not None else []:
                        await middleware.on_request(request)

                    # Do the processing from the EndPoint.
                    response = await endpoint.on_request(self._loop, request)

                    # Apply middleware post-processing
                    for middleware in request.app.middlewares if request.app is not None else []:
                        await middleware.on_response(request, response)

                    # Remove the body if this is a HEAD method.
                    if request.method == "HEAD":
                        response.body = ""

                    return response
                except Exception as err:
                    response = request.decorate_response(HTTPErrorResponse(500))
                    response.body = str(type(err)) + ": " + str(err)
                    return response
            else:
                response = request.decorate_response(HTTPErrorResponse(405))
                response.headers["Allow"] = ",".join(current_node)
                return response
        else:
            return request.decorate_response(HTTPErrorResponse(404))

    async def process_request(self, client: socket.socket, request: HTTPRequest) -> None:
        """
        Processes a single HTTPRequest object and returns a response.
        :param client: Client socket to write the response to.
        :param request: HTTPRequest to process.
        :return: None
        """
        response = await self.route_request(request)
        should_close = request.headers.get('Connection', '') != 'keep-alive'

        if should_close:
            response.headers['Connection'] = 'close'

        if len(response.body) > 32 and 'Accept-Encoding' in request.headers and 'Content-Encoding' not in response.headers:
            encodings = self._sort_by_qvalue(request.headers['Accept-Encoding'])
            for enc in encodings:
                if enc in SUPPORTED_ENCODING_TYPES:
                    response_body = response.body
                    if isinstance(response_body, str):
                        response_body = response_body.encode("utf-8")
                    response.body = await self._loop.run_in_executor(None, encode_bytes, enc, response_body)
                    response.headers['Content-Encoding'] = enc
                    break

        if "Content-Encoding" not in response.headers:
            response.headers["Content-Encoding"] = "identity"
        response.headers['Content-Length'] = str(len(response.body))

        try:
            await self._loop.sock_sendall(client, response.to_bytes())
            if should_close:
                client.close()
        except OSError:
            pass

    @staticmethod
    def _sort_by_qvalue(header: str) -> typing.List[str]:
        """
        Pulls apart a header value if it's a list and
        sort the values in the list by their qvalue.
        Note: This function parses but ignores level=# attributes
        as they are deprecated and rarely used.
        :param header: Header value to parse.
        :return: List of options sorted by their qvalue.
        """
        qvalues = [_QVALUE_REGEX.match(val).groups() for val in header.split(',')]
        values = [(float(qval if qval is not None else 1.0), value) for value, qval in qvalues]
        return [value for _, value in sorted(values, reverse=True)]
