class Base():
    def __init__(self, x: int) -> None:
        self.x = x
    def whatsx(self) -> int:
        return self.x

class Child(Base):
    def __init__(self, x: int) -> None:
        pass
        # Note: no call to super(), nor defining self.x.

c = Child(3)
print(c.whatsx())  # mypy does not catch undefined c.x
