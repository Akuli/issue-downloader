from typing import List, Optional
from mypy_extensions import safe_cast

def f(x: List[Optional[int]], n: int) -> List[Optional[int]]:
    # Mypy doesn't allow + for List[None] and List[Optional[int]], so we need a cast
    return safe_cast(List[Optional[int]], [None]) * n + x

x: Union[int, str] = 0
reveal_type(x)  # currently Union[int, str], but perhaps should be 'int'

x = safe_cast(Union[int, str], 0)  # Type safe!
reveal_type(x)  # Union[int, str]

