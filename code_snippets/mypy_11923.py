from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class A:
    x: Optional[List[int]] = field(default_factory=list)
