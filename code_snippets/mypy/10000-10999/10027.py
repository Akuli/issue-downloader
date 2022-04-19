from typing import Any, Type


def test(arg: Type[A]) -> None:
    return

def test2() -> None:
    for obj in (B, C):
        test(obj)  # ERROR IS HERE 


class A(Any):
    pass


class B(A):
    pass


class C(A):
    pass
