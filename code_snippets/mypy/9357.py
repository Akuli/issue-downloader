from typing import Callable, Generic, NamedTuple, Optional, Protocol, TypeVar


GenericType = TypeVar("GenericType")


class ClassOne(Protocol[GenericType]):
    def function(self, _: GenericType) -> Optional[GenericType]:
        return None


class ClassTwo(NamedTuple, Generic[GenericType]):
    not_: Callable[[ClassOne[GenericType]], Optional[ClassOne[GenericType]]]


def foobar(_: ClassOne[GenericType]):
    def function(_: ClassOne[GenericType]) -> Optional[ClassOne[GenericType]]:
        return None

    return ClassTwo(function)

