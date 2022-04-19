from typing import Callable, Generic, Type, TypeVar

XType = TypeVar('XType', bound=int)


class C(Generic[XType]):
    def f(self, x_init: XType) -> XType:
        return x_init


def combinator(c_cls: Type[C[XType]]) -> Callable[[C[XType], XType], XType]:
    old_f = c_cls.f

    def new_f(c: C[XType], x_init: XType) -> XType:
        return old_f(c, x_init)

    return new_f
