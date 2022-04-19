from dataclasses import dataclass
from typing import Generic, TypeVar, Union, NoReturn


def assert_never(a: NoReturn) -> NoReturn:
    raise AssertionError("Unhandled type: {}".format(type(a).__name__))


@dataclass
class Nothing:
    pass


T = TypeVar("T")


@dataclass
class Just(Generic[T]):
    value: T


Maybe = Union[Nothing, Just[T]]


def ok(a: Maybe[int]) -> None:
    if isinstance(a, Just):
        print(a.value)
    elif isinstance(a, Nothing):
        print("nothing")
    else:
        assert_never(a)


def ko(a: Maybe[int]) -> None:
    if isinstance(a, Nothing):
        print("nothing")
    elif isinstance(a, Just):
        print(a.value)
    else:
        assert_never(a)
