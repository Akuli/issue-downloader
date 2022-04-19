from abc import abstractmethod
from typing import TypeVar

from attr import attrs
from typing_extensions import Protocol

T = TypeVar("T")


@attrs(auto_attribs=True)
class Test(Protocol[T]):
    a: int

    @abstractmethod
    def transition_to(self, t: T):
        raise NotImplementedError
