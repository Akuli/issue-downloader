from typing import Any

class A: 
    pass

B: Any  # (Or from untyped_lib import B)

m: Any

if isinstance(m, (A, B)):
    reveal_type(m)
else:
    reveal_type(m)
