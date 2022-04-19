from types import MethodType
from typing import Callable

def describe(func: Callable[[], None]) -> str:
    if isinstance(func, MethodType):
        return 'bound method'
    else:
        return 'other callable'

class C:
    def m(self) -> None:
        pass

print(describe(C().m))
