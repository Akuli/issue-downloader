from abc import *
from fractions import *
from typing import *

Input = TypeVar('Input')
Output = TypeVar('Output')

class Base(Generic[Input, Output]):
    def do(self, input: Input) -> Output:
        # In reality do a bit more than just call "_operator".
        return self._operator(input)

    @abstractmethod
    def _operator(self, input: Input) -> Output:
        pass

class IntAdd(Base[int, int]):
    def _operator(self, input: int) -> int:
        return input + 1

class UnionAdd(Base[Union[int, Fraction], Union[int, Fraction]]):
    def _operator(self, input: Union[int, Fraction]) -> Union[int, Fraction]:
        return input + 1

reveal_type(IntAdd().do(1))
reveal_type(UnionAdd().do(1))

A = TypeVar('A', bound=Union[int, Fraction])

def do(input: A) -> A:
    return input + 1

reveal_type(do(1))
reveal_type(do(Fraction(2, 3)))

class SuperUnionAdd(Base[A, A]):
    def _operator(self, input: A) -> A:
        return input + 1

reveal_type(SuperUnionAdd().do(1))
reveal_type(SuperUnionAdd().do(Fraction(2, 3)))
