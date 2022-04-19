from abc import ABC
from typing import Generic, Protocol, Set, TypeVar

T = TypeVar('T')
V = TypeVar('V')


class HasData(Generic[T], Protocol):
    data: T


class ReplaceDataMixin(Generic[T]):
    def replace_data(self: HasData[T], new: T) -> None:
        self.data = new


class HasSet(Generic[V], ABC):
    def __init__(self, data: Set[V]):
        self.data: Set[V] = data


class MyClass(HasSet[float], ReplaceDataMixin[Set[float]]):
    pass


a = MyClass({1})
reveal_type(a.data)
reveal_type(a.replace_data)
