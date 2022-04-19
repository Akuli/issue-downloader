import enum
from dataclasses import dataclass
from typing import TypeVar, Generic, Type


M = TypeVar('M', bound="MyEnum")

class Meta(enum.EnumMeta):
    pass

class MyEnum(metaclass=Meta):
    ...

class Foo(enum.Enum, MyEnum):
    item1 = "1"
    item2 = "2"


class Bar(enum.Enum, MyEnum):
    item1 = "1"
    item2 = "2"

@dataclass
class Carrier(Generic[M]):
    meta: Type[M]
    instance: M


Carrier(Foo, Foo.item1)
Carrier(Foo, Bar.item1)  # should fail
