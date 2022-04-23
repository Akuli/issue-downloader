from typing import Optional
from typing import overload
from typing import Type

class A:
    pass

class Field:
    def __init__(self, attr: Optional["Field"] = None):
        self.attr = attr

    @property
    def crashing_property(self) -> Optional["Field"]:
        return self.attr

    @overload
    def __get__(self, instance: None, owner: Type["A"]) -> "Field":
        ...

    @overload
    def __get__(self, instance: "A", owner: Type["A"]) -> Optional["Field"]:
        ...

    def __get__(self, instance, owner):
        if not instance:
            return self
        return self.attr

f = Field()  # type: Field
f.attr  # Works fine
f.crashing_property  # Triggers "no overload variant"

@overload
def __get__(self, instance: "Field", owner: Type["Field"]):
    ...
