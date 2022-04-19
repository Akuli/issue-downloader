from typing import Tuple, Iterable

class NineCell:
    pass

class NineHouse(Tuple[NineCell, ...]):
    name: str

    def __new__(cls, name: str, iterable: Iterable[NineCell]) -> "NineHouse":
        self = super().__new__(cls, iterable)
        self.name = name
        return self
