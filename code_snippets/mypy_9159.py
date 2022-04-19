from typing import Optional, Tuple, TypeVar

_T = TypeVar("_T")
_U = TypeVar("_U")


def promote_optional(tup: Tuple[Optional[_T], Optional[_U]]) -> Optional[Tuple[_T, _U]]:
    for val in tup:
        if val is None:
            return None
    return tup

def promote_optional2(tup: Tuple[Optional[_T], Optional[_U]]) -> Optional[Tuple[_T, _U]]:
    if tup[0] is None:
        return None
    if tup[1] is None:
        return None
    return tup
