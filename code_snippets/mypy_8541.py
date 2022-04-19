from typing import Tuple, Type, TypeVar

CoordsT = TypeVar('CoordsT', bound='Coords')
class Coords(Tuple[float, float, float]):
    def __new__(cls: Type[CoordsT]) -> CoordsT:

        reveal_type(super().__new__)
        # Revealed type is 'def [_T] (cls: Type[_T`-1], iterable: typing.Iterable[_T_co`1] =) -> _T`-1'
        reveal_type(tuple.__new__)
        # Revealed type is 'def [_T_co, _T] (cls: Type[_T`-1], iterable: typing.Iterable[_T_co`1] =) -> _T`-1'

        value = (0.0, 0.0, 0.0)
        result = tuple.__new__(cls, value)
        # fine
        super().__new__(cls, value)
        # error: Argument 2 to "__new__" of "tuple" has incompatible type "Tuple[float, float, float]"; expected "Iterable[_T_co]"

        return result
