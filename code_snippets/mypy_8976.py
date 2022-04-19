from dataclasses import dataclass


@dataclass(frozen=True)
class Foo:
    attr: int


@dataclass(frozen=True)
class Bar(Foo):
    def attr(self) -> int:
        return 1
