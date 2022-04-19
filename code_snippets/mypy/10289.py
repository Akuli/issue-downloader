from typing import *

class Foo(Protocol):
    @property
    def foo(self) -> int:
        ...

class Bar:
    foo : ClassVar[int] = 42

x : Foo = Bar()
