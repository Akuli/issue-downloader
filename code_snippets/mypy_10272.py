from ctypes import Structure

from typing import Iterable


class S(Structure):
    pass


s = S()

if isinstance(s, Iterable):
    for _ in s:
        pass

