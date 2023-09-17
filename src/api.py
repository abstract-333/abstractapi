from typing import Any, Iterable, Callable, Union

from parse import parse
from webob import Request, Response


class API:
    def __init__(self):
        self.routes = {}

    def route(self, path: str):

        def wrapper(handler: Callable) -> Callable:
            self.routes[path] = handler
            return handler

        return wrapper

    def __call__(self, environ: dict, start_response: Any) -> Iterable:
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request: Request) -> Response:
        response = Response()
        handler, kwargs = self.find_handler(request.path)
        if handler is not None:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)
        return response

    def find_handler(self, request_path: str) -> Union[tuple[Callable, dict[str, str]], tuple[None, None]]:
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        return None, None

    def default_response(self, response: Response):
        response.status_code = 404
        response.text = "Not Found"
