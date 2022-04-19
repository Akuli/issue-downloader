from typing import Optional, List

def f1(a: Optional[int], b: int)->int:
    assert a is not None
    b = a
    return b

def f2(a: List[Optional[int]], i: int, b: int)->int:
    assert a[i] is not None
    b = a[i]
    return b

def f3(a: List[Optional[int]], i: int, b: int)->int:
    ai = a[i]
    assert ai is not None
    b = ai
    return b
