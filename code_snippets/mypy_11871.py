from typing import Self

class Widget:
    def add_thing(self, value: str) -> Self:
        self.value = value
        return self



from typing import TypeVar

TWidget = TypeVar("TWidget", bound="Widget")

class Widget:
    def add_thing(self: TWidget, value: str) -> TWidget:
        self.value = value
        return self


