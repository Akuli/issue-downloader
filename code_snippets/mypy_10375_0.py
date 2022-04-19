from typing import List

class A:
    a: List[int]

class B(A):
    a = []  # error: Need type annotation for 'a' (hint: "a: List[<type>] = ...")
