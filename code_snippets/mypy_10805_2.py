T = TypeVar('T', bound=Callable[..., Any])

class CountedFunction(Protocol[T]):
    __call__: T
    count: int

def counter(func: T) -> CountedFunction[T]: ...
