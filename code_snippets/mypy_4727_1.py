class A:
    def world(self) -> None:
        self.x = True

    def hello(self) -> None:
        if self.x:
            self.x = False
