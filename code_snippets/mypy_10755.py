# test_case.py
from numbers import Real
from operator import floordiv, mul, truediv
from typing import NamedTuple, Union

_OperandT = Union[float, Real]
# _OperandT = Real  # <- results in the same error
# _OperandT = float  # <- this works

class Spam(NamedTuple):
    value: _OperandT

    def __floordiv__(self, other: _OperandT) -> "Spam":
        return Spam(floordiv(self.value, other))

    def __rfloordiv__(self, other: _OperandT) -> "Spam":  # <- this presents an error …
        return Spam(floordiv(other, self.value))

    def __mul__(self, other: _OperandT) -> "Spam":
        return Spam(mul(self.value, other))

    def __rmul__(self, other: _OperandT) -> "Spam":  # <- … but this is just fine …
        return Spam(mul(other, self.value))

    def __truediv__(self, other: _OperandT) -> "Spam":
        return Spam(truediv(self.value, other))

    def __rtruediv__(self, other: _OperandT) -> "Spam":  # <- … and so is this
        return Spam(truediv(other, self.value))
