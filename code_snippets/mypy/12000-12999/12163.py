from typing import TypeVar, final

@final
class A:
    def __init__(self,value: str) -> None: ...

@final
class B: 
    def __init__(self,value: int) -> None: ...

T = TypeVar("T", A, B)

def foo(cls: type[T]) -> T:
    if issubclass(cls, A):
        return cls("") # error: Argument 1 to <subclass of "B" and "A"> has incompatible type "str"; expected "int
        # return cls(1) # error: Argument 1 to "A" has incompatible type "int"; expected "str
        # return A("") # error: Incompatible return value type (got "A", expected "B")
        # return B("") # error: Incompatible return value type (got "B", expected "A")
    else:
        return cls(1)
