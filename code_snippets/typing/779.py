SpecialReturn[int, bool, str]

Annotated[Tuple[int, bool, str], 'special return!']

class SpecialReturn():
    def __class_getitem__(self, params: Tuple[Any, ...]) -> Tuple[Any, ...]:
        return typing.cast(
            Tuple[Any, ...],
            _typing.Annotated[
                typing.Tuple.__getitem__(params),
                'multiple_return',
            ]
        )

import typing

from typing import Annotated, Any, Tuple


class SpecialReturn():
    def __class_getitem__(self, params: Tuple[Any, ...]) -> Tuple[Any, ...]:
        return typing.cast(
            Tuple[Any, ...],
            Annotated[
                typing.Tuple.__getitem__(params),
                'multiple_return',
            ]
        )


def test() -> SpecialReturn[int, int]:
    return 1, 2

from typing import Tuple


class SpecialReturn(Tuple):
    pass


def test() -> SpecialReturn[int, int]:
    return 1, 2
