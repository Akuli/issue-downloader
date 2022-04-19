from typing import Any, Callable, TypeVar

T = TypeVar('T', bound=Callable[..., Any])

def deco(f: T) -> T:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print('called')
        return f(*args, **kwargs)
    return wrapper  # Maybe this should be okay
