from dataclasses import field, dataclass

@dataclass
class C:
    some_int: int
    some_str: str = field(metadata={"doc": "foo"})
    another_int: int

c = C(42, "bla", 43)
