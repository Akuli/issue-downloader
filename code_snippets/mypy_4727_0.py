class A:
    def hello(self) -> None:
        if self.x:
            self.x = False

    def world(self) -> None:
        self.x = True
