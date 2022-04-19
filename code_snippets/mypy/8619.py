import operator
from functools import partialmethod


class IntCmp:
    def __init__(self, value):
        self._value = value

    def _cmp(self, opr, other: int) -> bool:
        if isinstance(other, int):
            return opr(self._value, other)
        return NotImplemented

    __eq__ = partialmethod(_cmp, operator.eq)  # Incompatible types in assignment (expression has type "partialmethod[bool]", base class "object" defined the type as "Callable[[object, object], bool]")
    __ne__ = partialmethod(_cmp, operator.ne)  # Incompatible types in assignment (expression has type "partialmethod[bool]", base class "object" defined the type as "Callable[[object, object], bool]")
    # rest of the comparison operators (lt, le, gt, ge) type checks correctly


c = IntCmp(1)
assert c == 1  # Cannot determine type of '__eq__'
