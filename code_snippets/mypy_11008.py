class X:
    def __init__(self):
        self._foo = 123

    def get_foo(self) -> int:
        return self._foo

    foo = property(get_foo)

    @foo.setter
    def foo(self, value: int) -> None:
        self._foo = value
