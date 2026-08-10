from typing import Any, TypedDict

from httpx import Client, URL, QueryParams, Response


class HttpClientExtensions(TypedDict, total=False):
    route: str


class HttpClient:
    def __init__(self, client: Client):
        self.client = client

    def get(
            self,
            path: URL | str,
            params: QueryParams | None = None,
            extensions: HttpClientExtensions | None = None
    ) -> Response:
        return self.client.get(path, params=params, extensions=extensions)

    def post(
            self,
            path: URL | str,
            body: Any = None,
            params: QueryParams | None = None,
            extensions: HttpClientExtensions | None = None
    ) -> Response:
        return self.client.post(path, params=params, json=body, extensions=extensions)
