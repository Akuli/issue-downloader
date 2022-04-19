from enum import Enum

class MyEnum(Enum):
    a = 1
    b = 2
    c = 3

some_func(MyEnum.a.value)

from typing import Enum

class MyEnum(Enum[int]):
    a = 1
    b = 2

some_func(MyEnum.a.value)
