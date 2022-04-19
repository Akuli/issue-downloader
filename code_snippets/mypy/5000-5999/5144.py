from typing import ClassVar, Type, Generic, TypeVar

_T = TypeVar('_T')

class Array(Generic[_T]):
    _length_: ClassVar[int]
    _type_: ClassVar[Type[_T]]

def generate() -> Type[Array[float]]:
    pass

generate()._type_(3)
