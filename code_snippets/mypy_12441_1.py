from dataclasses import dataclass
from a import A


@dataclass
class B(A):
    c: str

