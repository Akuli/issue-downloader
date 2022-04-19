from typing import Callable, NamedTuple

class Foo(NamedTuple):
    x: int

    def __call__(self) -> int:
        return self.x

foo: Callable[[], int] = Foo(42)
