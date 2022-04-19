from abc import ABC, abstractmethod
from typing import Any, Awaitable, Callable, TypeVar, cast

T = TypeVar('T')


def dec(args: Any) -> Callable[..., Awaitable[T]]:
    def dec2(f: Callable[..., Awaitable[T]]) -> Awaitable[T]:
        async def wrapper(*args:Any, **kwargs:Any) -> T:
            print(args)

            return cast(T, await f(*args, **kwargs))
        return cast(Awaitable[T], wrapper)
    return dec2


class A(ABC):
    @abstractmethod
    async def fn(self) -> 'bool':
        pass

class B(A):
    @dec('hi')
    async def fn(self) -> 'bool':
        return True


class C(A):
    @dec('hi')
    async def fn(self) -> 'bool':
        return False
