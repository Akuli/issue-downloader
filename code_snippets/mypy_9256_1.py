from types import coroutine
from typing import Any, Iterator

@coroutine
def my_coro_func() -> Iterator[None]:
    yield None

async def my_async_func() -> None:
    await my_coro_func()
