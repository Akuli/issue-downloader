T = TypeVar("T")

class SupportsSub(Protocol[T]):
    def __sub__(self: T, other: T) -> T:
        ...

class Fake:
    def __sub__(self, other: int) -> int: return 21
    
a: SupportsSub[int] = Fake()
