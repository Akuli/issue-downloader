from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar, Union

A = TypeVar('A')


class Base(Generic[A]):
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_stuff(self, a):
        # type: (A) -> None
        pass


class Foo(Generic[A], Base[A]):
    pass


class Bar(Generic[A], Base[A]):
    pass


class Baz(Foo[str], Bar[Union[str, int]]):
    def do_stuff(self, a):
        # type: (str) -> None
        return None
