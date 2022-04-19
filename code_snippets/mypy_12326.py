from typing import NamedTuple, Optional

class Foo(NamedTuple):
    bar: int = 0
    baz: str = ""

class MyClass():
    __slots__ = ['var1', 'var2', 'var3']

    def __init__(self, foo: Optional[Foo] = None) -> None:
        self._reset_state()
        if foo:
            self.var3 = foo

    def _reset_state(self) -> None:
        self.var1: int = 0
        self.var2: bool = False
        self.var3: Foo = Foo()
