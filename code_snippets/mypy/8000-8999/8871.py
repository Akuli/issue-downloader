T = TypeVar("T")


class A(Generic[T]):
    def __init__(self, a: T) -> None:
        self.a = a

    def __str__(self) -> str:
        if self.a is None:
            return "Foo"
        return "Bar"

class B(A[None]): ...
