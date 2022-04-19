from typing import Hashable

o1: type[object] = object
o2: type[int] = int
t1: type[type] = type
o3 = object
reveal_type(o1)  # note: Revealed type is "Type[builtins.object]"
reveal_type(o2)  # note: Revealed type is "Type[builtins.int]"
reveal_type(t1)  # note: Revealed type is "Type[builtins.type]"
reveal_type(o3)  # Revealed type is "def () -> builtins.object"
h1: Hashable = o1  # error: Incompatible types in assignment (expression has type "Type[object]", variable has type "Hashable")
h2: Hashable = o2  # error: Incompatible types in assignment (expression has type "Type[int]", variable has type "Hashable")
h3: Hashable = t1  # no errror
h4: Hashable = o3  # no errror
