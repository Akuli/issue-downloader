from typing import Type, TypeVar, TypedDict


T = TypeVar("T")


def f(cls: Type[T]) -> T:
    return cls()


class Foo(TypedDict):
    pass


f_foo: Foo = f(Foo)

reveal_type(f(Foo))
