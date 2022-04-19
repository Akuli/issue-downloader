
from __future__ import annotations

from typing import *


class B:
    pass


class A:
    name: Optional[Union[str, B]]


def foo(a: A):
    if isinstance(a.name, str):
        pass
    elif isinstance(a.name, B):
        pass
    else:
        raise AssertionError

    bar(a.name)


def bar(arg: Union[str, B]):
    pass
