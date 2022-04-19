N = TypeVar('N', numeric=True) # one idea for denoting type-level integers

class Vector(Generic[N]):
    def __init__(self, values: Iterable[float, N]) -> None:
        self.value = tuple(values)

    def __add__(self, other: Vector[N]) -> Vector[N]:
        return Vector(a + b for a, b in zip(self.values, other.values))

# ...more code...

def matmul(a: Matrix[N, M], b: Matrix[M, D]) -> Matrix[N, D]: ...
