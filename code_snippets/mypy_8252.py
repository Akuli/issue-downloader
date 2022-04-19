import abc
from typing import Generic, TypeVar


A = TypeVar('A')


class Expr(Generic[A], metaclass=abc.ABCMeta):
    pass


class Const(Expr[A]):
    value: A
    
    def __init__(self, value: A):
        self.value = value


class Add(Expr[int]):
    left: Expr[int]
    right: Expr[int]
    
    def __init__(self, left: Expr[int], right: Expr[int]):
        self.left = left
        self.right = right


def eval(e: Expr[A]) -> A:
    if isinstance(e, Const):
        # reveal_type(e)  # => Const[Any]
        return e.value
    elif isinstance(e, Add):
        # reveal_type(e)  # => <nothing>
        return eval(e.left) + eval(e.right)
        # error: <nothing> has no attribute "left"
        # error: <nothing> has no attribute "right"
    else:
        assert False


example = Add(Const[int](2), Const[int](1))
print(eval(example))
