import asyncio
from typing import Awaitable, Callable, TypeVar, overload, cast, Generic

T = TypeVar("T", bound=object)


class Async(Generic[T]):
    def __init__(self, f: Callable[[int], Awaitable[T]]):
        ...


class Sync(Generic[T]):
    def __init__(self, f: Callable[[int], T]):
        ...


@overload
def supposed_overlap(f: Callable[[int], Awaitable[T]]) -> Async[T]:
    ...

@overload
def supposed_overlap(f: Callable[[int], T]) -> Sync[T]:
    ...

def supposed_overlap(f: Callable[[int], Awaitable[T] | T]) -> Async[T] | Sync[T]:
    if asyncio.iscoroutinefunction(f):
        return Async(cast(Callable[[int], Awaitable[T]], f))
    else:
        return Sync(cast(Callable[[int], T], f))


@supposed_overlap
async def something_async(value: int) -> float:
    return 1.1


@supposed_overlap
def something_sync(value: int) -> str:
    return "1.1"


reveal_type(something_async)
reveal_type(something_sync)
