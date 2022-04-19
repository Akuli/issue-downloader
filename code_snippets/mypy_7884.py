
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

from __future__ import annotations

from typing import *


class B:
    pass


class A:
    name: Optional[Union[str, B]]


def foo(a: A):
    a_name = a.name

    if isinstance(a_name, str):
        pass
    elif isinstance(a_name, B):
        pass
    else:
        raise AssertionError

    bar(a_name)


def bar(arg: Union[str, B]):
    pass

