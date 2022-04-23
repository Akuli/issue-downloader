import pkg
pkg.utils.bar1(pkg.foo1())

__all__ = ('foo1', 'foo2')

from .module1 import foo1
from .module2 import foo2

def foo1() -> int:
    num = 1
    return num

from .utils import bar2

def foo2() -> str:
    num = 2
    return bar2(num)

def bar1(num: int) -> str:
    return 'a'

def bar2(num: int) -> str:
    return 'b'
