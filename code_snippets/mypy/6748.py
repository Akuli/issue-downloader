from typing import Generic, TypeVar, Callable

R = TypeVar('R')
L = TypeVar('L')
T = TypeVar('T')
E = TypeVar('E')


class Either(Generic[L, R]):

    def map(self, f):
        # type: (Callable[[R], T]) -> Either[L, T]
        # reveal_type(self.bimap)               # a
        # return self.bimap(lambda x: x, f)     # b
        y = self.bimap(lambda x: x, f)          # c (includes following line)
        return y

    def bimap(self, f, g):
        # type: (Callable[[L], E], Callable[[R], T]) -> Either[E, T]
        if isinstance(self, Left):
            return self.left(f(self.val))
        elif isinstance(self, Right):
            return self.right(g(self.val))
        assert False

    @classmethod
    def left(cls, lft):
        # type: (L) -> Either[L, R]
        return Left(lft)

    @classmethod
    def right(cls, rght):
        # type: (R) -> Either[L, R]
        return Right(rght)


class Left(Either[L, R]):
    def __init__(self, left):
        # type: (L) -> None
        self.val = left


class Right(Either[L, R]):
    def __init__(self, right):
        # type: (R) -> None
        self.val = right
