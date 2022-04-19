import typing

K = typing.TypeVar('K')

@typing.overload
def foo() -> None: ...

@typing.overload
def foo(k: K) -> K: ...
