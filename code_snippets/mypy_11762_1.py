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
