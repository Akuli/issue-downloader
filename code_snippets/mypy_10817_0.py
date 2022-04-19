from typing import TypeVar

class A:
    pass
class B(A):
    pass

QBT = TypeVar("QBT", bound=A)

def fn(t: QBT) -> QBT:
    if not isinstance(t, B):
        raise NotImplementedError
    return t # <- Incompatible types in "return" (actual type "B", expected type "QBT")
