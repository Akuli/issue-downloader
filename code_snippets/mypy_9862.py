import functools
from typing import Generic, TypeVar

T = TypeVar("T")


class A(Generic[T]):
    @property
    def field1(self) -> T:
        raise NotImplementedError

    @functools.cached_property
    def field2(self) -> T:
        raise NotImplementedError


class B(A[None]):
    @property
    def field1(self) -> None:
        return None

    @functools.cached_property
    def field2(self) -> None:
        return None
