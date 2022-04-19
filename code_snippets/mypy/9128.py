from typing import Dict, Any

params: Dict[str, Any] = {}
a: Dict[str, Any] = params.get("abc", set())
reveal_type(a)
