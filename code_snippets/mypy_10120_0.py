import typing

@typing.overload
def foo() -> None: ...

K = typing.TypeVar('K')
@typing.overload
def foo(k: K) -> K: ...
