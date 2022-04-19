import dataclasses as dtc
import typing as tp

T = tp.TypeVar('T', int, str, covariant=True)

@dtc.dataclass(frozen=True)
class C(tp.Generic[T]):
    c: type[T]

c_decision: dict[bool, C] = {
    True: C(int),
    False: C(str),
}

reveal_type(c_decision[True])
reveal_type(c_decision[False])

c_decision = {
    True: C(int),
    False: C(str),
}

