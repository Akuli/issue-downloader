from typing import Generic, TypeVar

T = TypeVar('T')
U = TypeVar('U')

class Data(Generic[T]): ...

class Container(Generic[T]):
    def clone(self: U) -> U: ...

class Example(Generic[T]):
    def example(self) -> None:
        container = Container[Data[T]]()
        clone = container.clone()
        reveal_type(container)
        reveal_type(clone)
