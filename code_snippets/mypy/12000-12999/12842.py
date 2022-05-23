from typing import Generic, TypeVar

T_co = TypeVar("T_co", covariant=True)

class FooGeneric(Generic[T_co]):
    pass

def accepts_foo(x: FooGeneric[T_co]) -> None:
    pass
