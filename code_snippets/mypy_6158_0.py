class CustomProperty(property):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        super().__init__(fget, fset, fdel, doc)

class A:
    def __init__(self) -> None:
        self._val = 1

    @CustomProperty
    def val(self) -> int:
        return self._val

    @val.setter
    def val(self, v: int) -> None:
        self._val = v


def test_a() -> None:
    print(A.val)
