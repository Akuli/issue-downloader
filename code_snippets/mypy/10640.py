from dataclasses import dataclass, field
from typing import List

@dataclass
class FilterExpression:
    match_type: str
    field: str
    value: List[str] = field(default_factory=list)
