from typing import Protocol

class SomeProtocol(Protocol):
    y : int
    x : int = 3

class Class(SomeProtocol):
    pass

def test1() -> None:
    y: int = Class.y  # runtime error. mypy should catch it?

def test2() -> None:
    x: int = Class.x  # runs fine, but should probably be a mypy error?
