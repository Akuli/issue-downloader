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

[mypy]

pretty = True
show_error_codes = True
strict = True
disallow_any_unimported = True
disallow_any_expr = True
disallow_any_decorated = True
disallow_any_explicit = True
no_warn_no_return = True
warn_unreachable = True

