from __future__ import annotations
from typing import Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class A:
  a: Optional[A]
