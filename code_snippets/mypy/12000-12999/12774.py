import attr
from typing import Any

def my_attr_s(cls, kw_only: bool = True) -> Any:  # Added to attr_class_makers using "fake plugin".
    return attr.s(kw_only=kw_only)(cls)

def my_attr_ib(**kwargs) -> Any:  # Added to attr_attrib_makers using "fake plugin".
    return attr.ib(**kwargs)

@my_attr_s
class A:
    optional: str = my_attr_ib(default="This attrib is not required now.")

@my_attr_s
class B(A):
    required: str = my_attr_ib()
