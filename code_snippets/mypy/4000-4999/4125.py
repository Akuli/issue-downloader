class Foo:
    def __init__(self) -> None:
        self.x = 42

class Bar(Foo):
    def __init__(self) -> None:
        self.y = 9000

    @property
    def x(self) -> int:
        print('got x!!!')
        return self.y

    @x.setter
    def x(self, value: int) -> None:
        print('set x!!!')
        self.y = value
