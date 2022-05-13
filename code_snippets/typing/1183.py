import asyncio
from typing import Any, Coroutine, Generic, TypeVar

from httpx import AsyncClient, Client, Response

ClientT = TypeVar("ClientT", bound=Client | AsyncClient)



class API(Generic[ClientT]):
    client: ClientT

    def __init__(self, client: ClientT) -> None:
        self.client = client

    def get_items(self) -> Response | Coroutine[Any, Any, Response]:
        return self.client.request('get', 'https://example.com/api/v1/get_items')


response = API[Client](Client()).get_items()
response.json()  # Item "Coroutine[Any, Any, Response]" of "Union[Response, Coroutine[Any, Any, Response]]" has no attribute "json"  [union-attr]

response_coroutine = API[AsyncClient](AsyncClient()).get_items()
asyncio.run(response_coroutine)  # Argument 1 to "run" has incompatible type "Union[Response, Coroutine[Any, Any, Response]]"; expected "Awaitable[Response]"  [arg-type]mypy(error)
