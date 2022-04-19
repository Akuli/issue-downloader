from typing import TypeVar , Tuple, Generic, Iterable, Callable

T = TypeVar('T', covariant=True)
S = TypeVar('S')


class _Base(Generic[T]):
    @classmethod
    def split(self, left, right):
        # type: (_Base[S], _Base[T]) -> _Base[Tuple[S, T]]
        return Split(left, right)

    @classmethod
    def merge_classmethod(cls, base, f):
        # type: (_Base[Iterable[T]], Callable[[Iterable[T]], T]) -> Merge[T]
        return Merge(base, f)

   # the type should use "S", not "T".
    def merge_method(self, f):
        # type: (_Base[Iterable[T]], Callable[[Iterable[T]], T]) -> Merge[T]
        return Merge(self, f)


class Split(_Base[Tuple[S, T]]):
    def __init__(self, left, right):
        # type: (_Base[S], _Base[T]) -> None
        pass


class Merge(_Base[T]):
    def __init__(self, base, f):
        # type: (_Base[Iterable[T]], Callable[[Iterable[T]], T]) -> None
        pass


def _sum(xs):
    # type: (Iterable[int]) -> int
    return sum(xs)


x = _Base()  # type: _Base[int]

# this typechecks
_Base.merge_classmethod(_Base.split(x, x), _sum)


# this doesn't:
# Argument 1 to "merge_method" of "_Base" has incompatible type "Callable[[Iterable[int]], int]"; expected "Callable[[Iterable[Tuple[int, int]]], Tuple[int, int]]"
_Base.split(x, x).merge_method(_sum)
