reveal_type("shaking")  # Literal["shaking"]?

reveal_type(int("1"))  # builtins.int*

from typing import TypeVar
T = TypeVar("T")
def foo(t: T) -> T:
    reveal_type(t)  # T`-1
