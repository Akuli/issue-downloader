class C:
    def __init__(self, a: str) -> None:
        if a is None:
            self.x = 123
        else:
            self.x = 456
