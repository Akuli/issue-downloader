from typing import Callable, TypeVar

class Base:
    pass

class Sub(Base):
    pass

class Other:
    pass

BT = TypeVar('BT', bound=Base)

def check(obj: BT) -> None:
    pass

check(Base())
check(Sub())
check(Other())

Factory = Callable[[], BT]

def f() -> Other:
    pass

fAny:   Factory        = f
fBase:  Factory[Base]  = f
fSub:   Factory[Sub]   = f
fOther: Factory[Other] = f
