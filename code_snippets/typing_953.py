from typing import TypeAlias

Str: TypeAlias = "str"
Int: TypeAlias = "int"

a: Str | Int = 0  # SUS ALERT

MyStr = NewType("MyStr", str)

from typing import NoReturn, TypedDict, TypeAlias, TypeVar, Generic, Protocol, etc, etc, etc, etc

from typing import TypeVar, Generic

T_cont = TypeVar("T_cont", contravariant=True, bound=str)

class A(Generic[T_cont]):
    ...

foo_result: int | str = foo(1, "a")
bar(foo_result)

bar(foo[int | str](1, "a"))

a: Literal[1, 2] = 1

a: 1 | 2 = 1

cast(int, a)

a: Callable[[int, str], bool]

A = int | str
A()  # is this valid?
foo(A)  # is this valid?
B: type[int | str] = int | str  # is this valid?

class A:
    a: int | str
A.__annotations__  # {'a': UnionType[int, str]}

a = UnionType(int, str)

from __future__ import annotations
from typing import get_type_hints

class A:
    x: "a" | "b"

get_type_hints(A)  # Currently will raise a TypeError
