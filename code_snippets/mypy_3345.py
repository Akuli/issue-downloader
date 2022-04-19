# Currently supported:
Tuple[int, int, int] # A tuple of 3 ints
Tuple[int, ...] # A tuple of any number of ints

# Proposed:
Tuple[int, 256] # A tuple of 256 ints

# Currently supported:
SboxType = Tuple[
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
]

# Proposed:
SboxType = Tuple[Tuple[int, 16], 8] # A tuple of 8 tuples of 16 ints each

N = TypeVar('N', numeric=True) # one idea for denoting type-level integers

class Vector(Generic[N]):
    def __init__(self, values: Iterable[float, N]) -> None:
        self.value = tuple(values)

    def __add__(self, other: Vector[N]) -> Vector[N]:
        return Vector(a + b for a, b in zip(self.values, other.values))

# ...more code...

def matmul(a: Matrix[N, M], b: Matrix[M, D]) -> Matrix[N, D]: ...

# Vector concatenation (relevant: http://stackoverflow.com/q/43292197/1974654)
def concat(a: Vector[N], b: Vector[M]) -> Vector[N+M]: ...

# The `zip` builtin (based on the typeshed stub)
@overload
def zip(iter1: Iterable[_T1, N1],
        iter2: Iterable[_T2, N2]) -> Iterator[Tuple[_T1, _T2], min(N1, N2)]: ...

# HDL-like bit vector operations
def add(a: BitVec[N], b: BitVec[M]) -> BitVec[max(N, M) + 1]: ...

