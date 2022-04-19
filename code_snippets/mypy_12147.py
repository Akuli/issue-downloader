from typing import Any

a: Any

a = {1: 2}  # error: Expression type contains "Any" (has type "Dict[Any, Any]")
