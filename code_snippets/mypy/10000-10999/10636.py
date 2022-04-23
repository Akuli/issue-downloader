var: Optional[List[Optional[int]]] = [1,2]  # mypy has no issue with this

from dataclasses import dataclass, field
from typing import Dict, Optional
@dataclass
class SubscriptedDict:
    opt_dict_opt: Optional[Dict[str, Optional[int]]] = field(default_factory=lambda: {"foo": 123}) 
