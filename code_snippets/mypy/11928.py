from typing import Generic, TypeVar, Iterable

T = TypeVar("T")
T1 = TypeVar("T1", bound=None)

class Test(Generic[T, T1]):
    def test(self) -> None:
        data1: list[T]
        data2: list[T] | list[T1]
        data3: list[T1] | list[T]
        
        reveal_type(tester(data1))  # list[T]
        reveal_type(tester(data2))  # list[object]
        reveal_type(tester(data3))  # list[Any]
        
        
def tester(a: Iterable[T]) -> list[T]: ...
