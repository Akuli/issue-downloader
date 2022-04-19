from abc import ABC, abstractmethod
from typing import TypeVar, Iterable, Iterator

T = TypeVar('T')


class MyABC(ABC):

    @property
    @abstractmethod
    def items(self) -> Iterable[T]: ...

    def my_method(self) -> Iterator[T]:
        for item in self.items:
            yield item
