from typing import Literal, overload


class A:
    def foo(self, bar: Literal["X"] | Literal["Y"]) -> int | bool:
        if bar == "X":
            return 1
        else:
            return True


class B(A):
    @overload
    def foo(self, bar: Literal["X"]) -> int:
        ...

    @overload
    def foo(self, bar: Literal["Y"]) -> bool:
        ...

    def foo(self, bar: Literal["X"] | Literal["Y"]) -> int | bool:
        return super().foo(bar)

class C:
    def foo(self, bar: bool | float) -> int | str:
        if isinstance(bar, bool):
            return 1
        else:
            return "A"


class D(C):
    @overload
    def foo(self, bar: bool) -> int:
        ...

    @overload
    def foo(self, bar: float) -> str:
        ...

    def foo(self, bar: bool | float) -> int | str:
        return super().foo(bar)

