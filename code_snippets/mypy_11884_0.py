import typing

@typing.runtime_checkable
class Foo(typing.Protocol):
    __slots__ = ()


class Bar:
    pass

_T = typing.TypeVar("_T", bound="Foo")


def foo(f: _T) -> _T:
    return f

print(issubclass(Bar, Foo))
print(isinstance(Bar(), Foo))
foo(Bar())
