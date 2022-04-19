from dataclasses import dataclass
from typing import TypeVar, Generic, Dict, Any

T = TypeVar("T")


class FloatValue:
    pass


@dataclass
class ValueByKey(Generic[T]):
    values: Dict[Any, T]


def foo(v: ValueByKey[FloatValue]):
    reveal_type(v.values)
    reveal_type(ValueByKey[FloatValue].__init__)
