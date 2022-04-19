from typing import Generic, TypeVar

T = TypeVar('T')

class C(Generic[T]):
    def foo(self, x: T) -> None:
        if isinstance(x, int):
            self.bar(x)

    def bar(self, x: T) -> None:
        pass
