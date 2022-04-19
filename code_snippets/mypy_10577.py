# $ cat mypy-bug.py
from typing import Protocol, Union
from typing_extensions import runtime_checkable
from operator import add as op_add

class Foo: pass

# FooAbleOperandT = Union[int, float, Foo, "FooAbleT"]  # <- this will work

@runtime_checkable
class FooAbleT(Protocol):
    FooAbleOperandT = Union[int, float, Foo, "FooAbleT"]  # <- this won't
    def __add__(self, other: FooAbleOperandT) -> Foo:
        return op_add(self.foo(), other)
    def __radd__(self, other: Union[int, float]) -> Foo:  # <- chokes here
        return op_add(other, self.foo())
    def foo(self) -> Foo: ...
