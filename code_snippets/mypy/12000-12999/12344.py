from typing import Protocol

class MixinProt(Protocol):
    def func(self) -> None:
        ...

class Mixin:
    def func(self: MixinProt) -> None:
        return super().func()
