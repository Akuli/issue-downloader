from typing import TypeVar


class A:
    pass


class B:
    pass


OperableT = TypeVar(
    "OperableT",
    A,
    B,
)


class Operator:
    def process(self, obj: OperableT) -> OperableT:
        if isinstance(obj, A):
            return A()
        elif isinstance(obj, B):
            return B()
