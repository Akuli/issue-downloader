T = TypeVar('T')
class Wrapper(Generic[T]):
    def __init__(self, x: T) -> None: pass

def test(x: Wrapper[MyProtocol]) -> None: pass
test(Wrapper(SomeClass()))
