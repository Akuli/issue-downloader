class Foo:
    def __init__(self, value:int) -> None:
        self.value = value

class Bar(Foo):
    def __init__(self) -> None:
        pass


a = Bar().value # runtime error
