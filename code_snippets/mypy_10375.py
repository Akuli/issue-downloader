from typing import List

class A:
    a: List[int]

class B(A):
    a = []  # error: Need type annotation for 'a' (hint: "a: List[<type>] = ...")

from typing import List

class A:
    def __init__(self) -> None:
        self.a: List[int]

class B(A):
    def __init__(self) -> None:
        super().__init__()
        self.a = []
