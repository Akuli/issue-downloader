from typing import Any, Union


class A:
    pass


class B(A):
    def __init__(self):
        self.member = 1


class C(A):
    def __init__(self):
        self.member = 2


def f(obj: A) -> int:
    if isinstance(obj, B):
        pass
    elif isinstance(obj, C):
        pass
    else:
        raise ValueError()
    return obj.member

from typing import Any, Union


class A:
    pass


class B(A):
    def __init__(self):
        self.member = 1


class C(A):
    def __init__(self):
        self.member = 2


def f(obj: A) -> Union[B, C]:
    if isinstance(obj, B):
        pass
    elif isinstance(obj, C):
        pass
    else:
        raise ValueError()
    return obj

