from dataclasses import dataclass

@dataclass
class A:
    a: int = 0

@dataclass
class B(A):
    a: int
    b: str
