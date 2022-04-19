from typing_extensions import Protocol, Literal


class Char(Protocol):
    def __len__(self) -> Literal[1]:
        ...


a: Char = "X"

