class C:
    def __new__(cls, x: int) -> C:
        self = object.__new__(cls)
        self.x: Final = x
        return self
