from typing import TypeVar, cast

class A:
    pass
class B(A):
    pass

QBT = TypeVar("QBT", bound=A)

def fn(t: QBT) -> QBT:
    if not isinstance(t, B):
        raise NotImplementedError
    return cast(QBT, t) # <- OK! on .8 its marked as redundant.
