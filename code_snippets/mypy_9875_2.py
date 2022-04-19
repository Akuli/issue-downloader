@dataclass
class C:
    some_int: int
    some_str: str = doc("foo")
    another_int: int
