from typing import Protocol


class P(Protocol):
    def foo(self, n: int = 666) -> None: ...


class F:
    def foo(self, n: int = 666) -> None: ...


class S:
    def foo(self, n: int = 999) -> None: ...


def bar(x: P) -> None: ...


bar(F())
bar(S())
