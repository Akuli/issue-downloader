
from typing import TypeVar

TWidget = TypeVar("TWidget", bound="Widget")

class Widget:
    def add_thing(self: TWidget, value: str) -> TWidget:
        self.value = value
        return self

