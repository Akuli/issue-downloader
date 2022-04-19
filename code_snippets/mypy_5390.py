from typing import *

class MyProtocol(Protocol):
    def foo(self) -> int: pass

class SomeClass:
    def foo(self) -> str: pass

def test(x: Type[MyProtocol]) -> None: pass

test(SomeClass)

def test(x: MyProtocol) -> None: pass
test(SomeClass())

T = TypeVar('T')
class Wrapper(Generic[T]):
    def __init__(self, x: T) -> None: pass

def test(x: Wrapper[MyProtocol]) -> None: pass
test(Wrapper(SomeClass()))
