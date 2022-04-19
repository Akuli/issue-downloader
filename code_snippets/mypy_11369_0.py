T = TypeVar("T")
R = TypeVar("R")
Decorator = Callable[[Callable[..., T]], Callable[..., R]]
