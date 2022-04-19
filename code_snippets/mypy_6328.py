from typing import Any, List

a = 0  # type: Any

x = filter(None, reveal_type(a))  # type: List[str]  # Error
x2 = filter(None, a)  # type: List[str]  # No error
