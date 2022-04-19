from typing import TypeVar, List

StrOrList = TypeVar('StrOrList', str, List[str])

def f(a: StrOrList) -> StrOrList:
    b = a if isinstance(a, list) else [a]
    return b if isinstance(a, list) else b[0]
