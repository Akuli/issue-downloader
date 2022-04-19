from typing import Union, Generic, TypeVar, overload

T = TypeVar("T")

class Foo(Generic[T]):
    pass

@overload
def expect(pattern: Foo[T]) -> None: ...

@overload
def expect(pattern: T) -> None: ...

def expect(pattern: Union[Foo[T], T]) -> None: return None
