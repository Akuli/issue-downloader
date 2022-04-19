from dataclasses import dataclass, InitVar
@dataclass
class MyClass:
    prop: InitVar[int]
    _prop: int

    def __post_init__(self, prop: int):
        self._prop = prop

    @property
    def prop(self) -> int:
        return self._prop
