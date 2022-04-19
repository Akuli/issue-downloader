from typing import Awaitable, Generic, TypeVar

T = TypeVar("T")

class Foo(Generic[T]):
    contents: T

def get_from(foo: Foo[T]) -> Awaitable[T]:
    async def get_it() -> T:
        return foo.contents
    return get_it()

async def test() -> None:
    foo = Foo[int]()
    foo.contents = 42
    assert 42 == await get_from(foo)
