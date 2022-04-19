import sys
from typing import TypeVar, Generic, overload

assert sys.version_info >= (3, 5)


class Foo(object):
    def __init__(self, dummy):
        self.dummy = dummy


class Bar(object):
    def __init__(self, dummy):
        self.dummy = dummy


class Apple(object):
    def __init__(self, dummy):
        self.dummy = dummy


class Pear(object):
    def __init__(self, dummy):
        self.dummy = dummy


Var1 = TypeVar('Var1', Foo, Apple)
Var2 = TypeVar('Var2', Bar, Pear)


@overload
def combine(left: Foo, right: Bar) -> None:
    ...


@overload
def combine(left: Apple, right: Pear) -> None:
    ...


def combine(left, right):
    print(left.dummy + " and " + right.dummy)


class MyClass(Generic[Var1, Var2]):
    def __init__(self, a: Var1) -> None:
        self.dummy = dummy  # type: Var1

    def add(self, other: Var2) -> None:
        combine(self.dummy, other)

