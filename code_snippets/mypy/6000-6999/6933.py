from typing import *

T = TypeVar('T')
InT = TypeVar('InT')
OutT = TypeVar('OutT')


class Transform(Generic[InT, OutT]):
    "Takes an input Collection and produces an output Collection"

    def __init__(self, fn: Callable[[InT], OutT]):
        self.fn = fn

    def call(self, arg: InT) -> OutT:
        return self.fn(arg)


def get_op(f: Callable[[InT], OutT]) -> Transform[InT, OutT]:
    "Get a Transform from a callable"
    return Transform(f)


class Collection(Generic[T]):
    "Collection of elements"

    def apply(self, op: Transform[T, OutT]) -> 'Collection[OutT]':
        """
        Apply the this Collection to a Transform and produce a new 
        output Collection
        """


# -- test:

def make_string(x: None) -> str:
    return 'foo'


def make_ones(x: T) -> Tuple[T, int]:
    return (x, 1)


c1: Collection = Collection()

str_op = get_op(make_string)
reveal_type(str_op)  # revealed: Transform[None, builtins.str*]

c2 = p1.apply(str_op)
reveal_type(c2)  # revealed: Collection[builtins.str*]

tuple_op = get_op(make_ones)
reveal_type(tuple_op)  # revealed: Transform[T`-1, Tuple[T`-1, builtins.int]]

c3 = c2.apply(tuple_op)
# Desired type is Collection[Tuple[builtins.str, builtins.int]]
reveal_type(c3)  # revealed: Collection[Tuple[T`-1, builtins.int]]

class Collection(Generic[T]):
    "Collection of elements"

    def apply(self, op: Transform[T, OutT]) -> 'Collection[OutT]':
        """
        Apply the this Collection to a Transform and produce a new 
        output Collection
        """
