from typing import List

class A:
    pass

class B(A):
    pass

def test(arg: List[A]) -> None:
    if all([isinstance(a, B) for a in arg]):
        test2(arg)

def test2(arg: List[B]) -> None:
    pass
