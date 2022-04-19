from dataclasses import dataclass, field

@dataclass
class Base:
    foo: bool = field()

@dataclass(frozen=True)
class Derived(Base):
    @property
    def foo(self):
        pass
