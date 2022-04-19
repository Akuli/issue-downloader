# coding: utf-8
# mypy: warn_return_any
# mypy: disallow_any_expr
# mypy: disallow_any_generics
from typing import Sequence

def getStringSequence(value:object) -> Sequence[str]:
    if isinstance(value, Sequence):
        reveal_type(value) # Revealed type is Sequence[Any]
        return value
    raise TypeError
