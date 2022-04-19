from typing import AbstractSet, Iterable, Optional, Set, TypeVar

T = TypeVar('T')

def intersection(seq: Iterable[AbstractSet[T]]) -> Optional[Set[T]]:
    ret = None
    for elem in seq:
        if ret is None:
            ret = set(elem)
        else:
            ret &= elem
    return ret
