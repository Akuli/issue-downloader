# test.py
from typing import Generic, Type, TypedDict, TypeVar


_TA = TypeVar("_TA")
_TB = TypeVar("_TB")


class GenericBase(Generic[_TA, _TB]):
    type_a: Type[_TA]
    type_b: Type[_TB]


A = TypedDict("A", {})
B = TypedDict("B", {})


class GenericChild(GenericBase[A, B]):
    type_a = A
    type_b = B

