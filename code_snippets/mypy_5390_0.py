from typing import *

class MyProtocol(Protocol):
    def foo(self) -> int: pass

class SomeClass:
    def foo(self) -> str: pass

def test(x: Type[MyProtocol]) -> None: pass

test(SomeClass)
