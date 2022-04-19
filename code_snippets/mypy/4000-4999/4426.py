class P(Protocol):
    x: int  # Note, no r.h.s.

class C(P):
    pass
class D(P):
    def __init__(self) -> None:
        self.x = 42

C()  # E: Cannot instantiate abstract class 'C' with abstract attribute 'x'
D()  # OK
