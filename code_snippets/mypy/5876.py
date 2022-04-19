from typing import Any

class A:
    # A method that accepts unspecified arguments and returns int
    def f(self, *args: Any, **kwargs: Any) -> int: pass

class B(A):
    def f(self, x: int) -> int: pass  # Should be okay

from typing import Any, Callable, TypeVar

T = TypeVar('T', bound=Callable[..., Any])

def deco(f: T) -> T:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print('called')
        return f(*args, **kwargs)
    return wrapper  # Maybe this should be okay
