A = TypeVar('A')
B = TypeVar('B')
F = TypeVar('F')

class M(Generic[F[X], A]):
    def x(fa: F[A], f: Callable[[A], B]) -> F[B]:
        return map(f, fa)

M().x([1], str)
