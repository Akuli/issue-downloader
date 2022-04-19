import dataclasses

from .mydc_base import MyDataclassBase


@dataclasses.dataclass
class MyDataclass(MyDataclassBase):
    extra_field: int


mydc = MyDataclass(my_field=None, extra_field=0)
