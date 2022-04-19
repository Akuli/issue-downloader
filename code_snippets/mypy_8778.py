class Foo:
    @classmethod
    def baz(cls):
        return cls.__name__


class Bar(Foo):
    pass

from typing import TypeVar
from .bar import Foo, Bar


FooType = TypeVar("FooType", bound=Foo)


def takes_foo(foo: FooType) -> FooType:
    print(type(foo).baz())
    return foo


class Foo2:
    @classmethod
    def baz(cls):
        return cls.__name__


class Bar2(Foo):
    pass


Foo2Type = TypeVar("Foo2Type", bound=Foo2)


def takes_foo2(foo: Foo2Type) -> Foo2Type:
    print(type(foo).baz())
    return foo

