from typing import final, Type, TypeVar, Union

@final
class A:
    def __init__(self, a: int) -> None:
        ...

@final
class B:
    def __init__(self, b: str) -> None:
        ...

U = Union[A, B]
T = TypeVar("T", A, B)

def f(x: Type[U]) -> U:
    if issubclass(x, A):
        reveal_type(x)
        # Revealed type is "A"
        return x(a=1)
    return x(b="a")

def g(x: Type[T]) -> T:
    if issubclass(x, A):
        reveal_type(x)
        # Revealed type is "A*"
        # Revealed type is "<subclass of "B" and "A">"
        return x(a=1)
        # Unexpected keyword argument "a" for <subclass of "B" and "A">
    return x(b="b")
