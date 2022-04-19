from typing import Sequence, TypeVar, Union

D = TypeVar("D")
E = TypeVar("E")


def get_first(values: Sequence[E], default: D = None) -> Union[E, D]:
    if len(values) == 0:
        return default
    else:
        return values[0]
