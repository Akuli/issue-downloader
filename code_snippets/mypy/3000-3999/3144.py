T = TypeVar('T')
class Outer(Generic[T]):
    class Inner:
        x: T  # E: Invalid type "test.T" (correct)
        def f(self, x: T) -> T: ... # ok (incorrect)
        def g(self) -> None:
            y: T  # E: Invalid type "test.T" (correct)
