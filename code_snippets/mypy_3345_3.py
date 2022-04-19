# Vector concatenation (relevant: http://stackoverflow.com/q/43292197/1974654)
def concat(a: Vector[N], b: Vector[M]) -> Vector[N+M]: ...

# The `zip` builtin (based on the typeshed stub)
@overload
def zip(iter1: Iterable[_T1, N1],
        iter2: Iterable[_T2, N2]) -> Iterator[Tuple[_T1, _T2], min(N1, N2)]: ...

# HDL-like bit vector operations
def add(a: BitVec[N], b: BitVec[M]) -> BitVec[max(N, M) + 1]: ...
