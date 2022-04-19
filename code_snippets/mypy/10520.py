class Possibility(Generic[T]):
    def __init__(self, produce: Callable[[], T]):
        self._produce = produce
    def produce(self) -> T:
        return self._produce()
def reject() -> NoReturn:
    raise RuntimeError
def nothing() -> Possibility[NoReturn]:
    return Possibility(lambda: reject())  # Error here
