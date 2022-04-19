from typing import Any

class A:
    # A method that accepts unspecified arguments and returns int
    def f(self, *args: Any, **kwargs: Any) -> int: pass

class B(A):
    def f(self, x: int) -> int: pass  # Should be okay
