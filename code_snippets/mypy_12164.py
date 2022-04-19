from typing import final
from abc import ABC, abstractmethod

class Foo(ABC):
    @final
    @abstractmethod
    def foo(self) -> None: ...
