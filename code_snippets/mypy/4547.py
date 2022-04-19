from typing import List

class A:
    x: List[str]

class B(A):
    x = []  # Need type annotation
