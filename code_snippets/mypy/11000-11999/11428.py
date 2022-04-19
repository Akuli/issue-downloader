from typing import Generic, TypeGuard, TypeVar, Union

L = TypeVar("L")
R = TypeVar("R")


class Left(Generic[L]):
    value: L

    def __init__(self, value: L):
        self.value = value


class Right(Generic[R]):
    value: R

    def __init__(self, value: R):
        self.value = value


LeftOrRight = Union[Left[L], Right[R]]


def is_left(obj: LeftOrRight[L, R]) -> TypeGuard[Left[L]]:
    return isinstance(obj, Left)


def is_right(obj: LeftOrRight[L, R]) -> TypeGuard[Right[R]]:
    return isinstance(obj, Right)


x: LeftOrRight[str, int] = Left("")
reveal_type(x)  # Revealed type is "Union[Left[builtins.str], Right[builtins.int]]"

if isinstance(x, Left):
    reveal_type(x)  # Revealed type is "Left[builtins.str]"
    x.value + ""  # only valid for str
else:
    reveal_type(x)  # Revealed type is "Right[builtins.int]"
    x.value + 10  # only valid for int

if is_left(x):
    reveal_type(x)  # Revealed type is "Left[L`-1]"
    x.value + ""  #  Unsupported left operand type for + ("L")  [operator]
else:
    reveal_type(x)  # Revealed type is "Union[Left[builtins.str], Right[builtins.int]]"
    x.value + 10  # Unsupported operand types for + ("str" and "int")  [operator]

