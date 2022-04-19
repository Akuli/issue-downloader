from __future__ import annotations

def f(a: int | str = None):
    pass

from typing import Union

def f(a: Union[int, str] = None):
    pass

