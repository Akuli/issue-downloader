from typing import Callable, TypeVar

T = TypeVar("T")

x = 1


def decorate(num: int) -> Callable[[T], T]:
    def thru(it: T) -> T:
        print("decorating", it, "with", num)
        return it
    return thru


class y(object):
    @decorate(x)
    def a(self) -> None:
        ...

    x = 2

    @decorate(x)
    def b(self) -> None:
        ...

    del x

    @decorate(x)
    def c(self) -> None:
        ...
