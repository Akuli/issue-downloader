# test_case1.py
from __future__ import annotations
from typing import Protocol, runtime_checkable

@runtime_checkable
class Foo(Protocol):
    __slots__ = ()
    def foo(self):
        ...

class Bar:
    __slots__ = ("_t",)
    def __init__(self):
        self._t = True
    def foo(self):
        pass

print(f"isinstance(Bar(), Foo) == {isinstance(Bar(), Foo)}")  # <- prints … == True
foo: Foo = Bar()  # <- errors here
