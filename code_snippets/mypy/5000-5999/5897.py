from typing import Type, TypeVar, TYPE_CHECKING


class A:
    def __init__(self, arg: int) -> None:
        self._arg = arg


class B(A):
    def __init__(self, arg: int) -> None:
        super().__init__(arg)


_TA = TypeVar('_TA', bound=A)


def get_entity(entity_class: Type[_TA], arg: int) -> _TA:
    if TYPE_CHECKING:
        reveal_type(entity_class)       # <- Revealed type is 'Type[_TA`-1]'
        reveal_type(entity_class(1))    # <- Revealed type is '_TA`-1'
    return entity_class(arg)


if __name__ == '__main__':
    print(get_entity(B, 3))
