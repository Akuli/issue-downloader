from typing import Self

class Widget:
    def add_thing(self, value: str) -> Self:
        self.value = value
        return self

