from abc import ABC, abstractmethod


class Foo(ABC):
    @abstractmethod
    @property
    def foo(self) -> int:
        ...
