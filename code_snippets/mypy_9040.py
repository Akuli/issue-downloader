from typing import Any, Optional


def foo(baz: Any) -> int:
    return 1


def bar1(baz: Any = 0) -> int:
    reveal_type(baz)
    baz = foo(baz)
    reveal_type(baz)
    return baz


def bar2(baz: Optional[Any] = 0) -> int:
    reveal_type(baz)
    baz = foo(baz)
    reveal_type(baz)
    return baz
