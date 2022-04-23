class A:
    def hello(self) -> None:
        if self.x:
            self.x = False

    def world(self) -> None:
        self.x = True

class A:
    def world(self) -> None:
        self.x = True

    def hello(self) -> None:
        if self.x:
            self.x = False

class A:
    def hello(self) -> None:
        if self.x:
            self.x = False  # type: bool

    def world(self) -> None:
        self.x = True
