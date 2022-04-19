class A:
    x = None
    y = None

    def __init__(self):  # Note: no annotation
        self.x = 1

    def g(self) -> None:
        self.y = 1

a = A()
reveal_type(a.x)  # None  <---- unexpected
reveal_type(a.y)  # Union[int, None]

if a.x is not None:
    1 + ''  # No error, because mypy considers this unreachable
