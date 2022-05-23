
from typing import Hashable, Mapping, Any, TypeVar

T = TypeVar("T", bound="A")

class A:
    def a(
        self: T,
        x: Hashable | Mapping[Any, Any]
    ) -> T:
        return self


s = A()
s.a("asd")  # ok
s.a({"a": 1})  # fails
