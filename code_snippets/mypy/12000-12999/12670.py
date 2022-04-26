from collections.abc import Iterator
from contextlib import contextmanager

class C:
    def __init__(self) -> None:
        self.x: None | int = None

    @contextmanager
    def f(self) -> Iterator[None]:
        self.x = None
        try:
            yield
        finally:
            if self.x is None:
                raise ValueError
            print("ok")  # error: Statement is unreachable  [unreachable]


c = C()
with c.f():
    c.x = 1
