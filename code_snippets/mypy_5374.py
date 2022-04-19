import abc
from dataclasses import dataclass


@dataclass  # error: Only concrete class can be given where "Type[Abstract]" is expected
class Abstract(metaclass=abc.ABCMeta):
    a: str

    @abc.abstractmethod
    def c(self) -> None:
        pass


@dataclass
class Concrete(Abstract):
    b: str

    def c(self) -> None:
        pass


instance = Concrete(a='hello', b='world')
