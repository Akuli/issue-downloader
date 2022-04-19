from typing import TypeVar, Type, Iterable, Iterator
T = TypeVar('T')
class M(type):
    def __iter__(self: Type[T]) -> Iterator[T]: raise Exception
class A(metaclass=M): pass
x: Iterable[A] = A  # fine
y: Iterable[str] = A  # should be rejected, but it is not
