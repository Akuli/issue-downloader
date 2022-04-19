import typing
T = typing.TypeVar("T")

class Test(typing.NamedTuple, typing.Generic[T]):
    a: T

x: Test[int] = Test(a=1) # TypeError: 'type' object is not subscriptable
