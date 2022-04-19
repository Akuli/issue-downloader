from typing import Any, Dict, Literal
kw: Dict[Literal["a", "b"], Any]
def func(a, b):
    pass
func(**kw)
