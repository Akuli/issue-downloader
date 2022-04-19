from typing import Mapping, Any, Optional

x: Optional[Any]
m: Mapping[str, int]

m.get(x)
# error: Argument 1 to "get" of "Mapping" has incompatible type "Optional[Any]"; expected "str"
