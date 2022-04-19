import typing

@typing.overload
def foo() -> None: ...

K = typing.TypeVar('K')
@typing.overload
def foo(k: K) -> K: ...

import typing

K = typing.TypeVar('K')

@typing.overload
def foo() -> None: ...

@typing.overload
def foo(k: K) -> K: ...

