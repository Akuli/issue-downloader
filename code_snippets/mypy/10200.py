from .mydc import MyDataclass


class MyClass:
    pass


import dataclasses
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .myclass import MyClass


@dataclasses.dataclass
class MyDataclassBase:
    my_field: Optional['MyClass']

import dataclasses

from .mydc_base import MyDataclassBase


@dataclasses.dataclass
class MyDataclass(MyDataclassBase):
    extra_field: int


mydc = MyDataclass(my_field=None, extra_field=0)

