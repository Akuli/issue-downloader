from typing import Hashable, Any

t1: type[Any] = type
h1: Hashable = t1  # error: Incompatible types in assignment (expression has type "Type[Any]", variable has type "Hashable")
