class B:
    def __init__(self) -> None:
        self._val = 1

    @property
    def val(self) -> int:
        return self._val

    @val.setter
    def val(self, v: int) -> None:
        self._val = v

def test_b() -> None:
    print(B.val)
