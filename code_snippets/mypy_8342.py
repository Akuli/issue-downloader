from typing import TypeVar


T = TypeVar("T", bound="Number")


class Number:
    def __abs__(self: T):
        return self

    def square(self: T) -> T:
        return self


def myabs(x: T) -> T:
    return abs(x)


x = myabs(Number())
x.square()

from typing import TypeVar


T = TypeVar("T", bound="Number")


class Number:
    def __abs__(self: T) -> T:
        return self

    def square(self: T) -> T:
        return self


def myabs(x: T) -> T:
    return abs(x)


x = myabs(Number())
x.square()
