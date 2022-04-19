from dataclasses import dataclass

@dataclass
class Foo:
    bar: str

    @classmethod
    def bar(cls) -> "Foo":
        return cls()
