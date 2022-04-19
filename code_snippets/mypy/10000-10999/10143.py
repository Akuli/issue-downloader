# pyright: strict

from typing import Literal, Union, overload

class Parent: ...
class Child(Parent): ...

# Test 1: Literal subtype
@overload
def foo1(x: Literal[3]) -> int: ...
@overload
def foo1(x: int) -> str: ...

# Test 2: Subclass subtype
@overload
def foo2(x: Child) -> str: ...
@overload
def foo2(x: Parent) -> int: ...

# Test 3: Implicit subtype
@overload
def foo3(x: int) -> str: ...  # Mypy does not report error here
@overload
def foo3(x: float) -> int: ...

# Test 4: Union subtype
@overload
def foo4(x: int) -> str: ...
@overload
def foo4(x: Union[int, str]) -> int: ...
