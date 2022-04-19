from __future__ import annotations
from typing import NamedTuple, Protocol, Optional

class Simple:
    two: Optional[int]

    def as_simpl_verified(self) -> SimpleVerified:
        assert self.two is not None
        return self

class SimpleVerified(Protocol):
    two: int
