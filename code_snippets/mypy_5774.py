class C:
    def __new__(cls, x: int) -> C:
        self = object.__new__(cls)
        self.x: Final = x
        return self

class C:
    x: Final[int]
    def __new__(cls) -> C:
        self = object.__new__(cls)
        self.x: Final = 1
        return self
