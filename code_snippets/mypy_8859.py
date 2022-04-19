import test


class C(test.A, test.B):
    pass

from .a import *
from .b import *

from . import a
from . import b


__all__ = a.__all__ + b.__all__

class A:
    pass


__all__ = ["A"]

class B:
    pass


__all__ = ["B"]

