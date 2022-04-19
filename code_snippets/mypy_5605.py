A = TypeVar("A")
f: Optional[Callable[[str], A]] = None
f = lambda x: str(x)
