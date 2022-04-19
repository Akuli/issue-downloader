from typing import Final, Optional


class Foo:
    a: Final[Optional[int]]

    def __init__(self, v: int) -> None:
        if v == 0:
            self.a = None
        else:
            self.a = v  # error: Cannot assign to final attribute "a"  [misc]
