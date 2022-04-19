from abc import ABC, abstractmethod
from typing import Type


class ISolution(ABC):
    @abstractmethod
    def __init__(self, b: int):
        pass

    @abstractmethod
    def func1(self, a: int) -> int:
        pass


class MySolution(ISolution):
    def __init__(self, b: int):
        self._b = b

    def func1(self, a: int) -> int:
        return a + self._b


class IHolder(ABC):
    @property
    @classmethod
    @abstractmethod
    def SolutionClass(cls) -> Type[ISolution]:
        pass

    # SolutionClass: Type[ISolution]

    @abstractmethod
    def __init__(self, c: int):
        pass

    @abstractmethod
    def cval(self) -> int:
        pass


class Main(IHolder):
    SolutionClass = MySolution

    def __init__(self, c: int):
        self._c = c

    def cval(self) -> int:
        return self._c


def check(holderclass: Type[IHolder], a: int, b: int, c: int) -> bool:
    holder = holderclass(c)
    solclass: Type[ISolution] = holderclass.SolutionClass
    return solclass(b).func1(a) == holder.cval()


print("should be true ", check(Main, 5, 5, 10))
print("should be false ", check(Main, 3, 4, 10))
