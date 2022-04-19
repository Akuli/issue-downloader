from typing import Dict
a: Dict[str, str] = {"x": "y"}
b: Dict[str, str] = {"y": "z"}
def f(x: str) -> str:
    f_a = a.get(x)
    reveal_type(f_a)  # Optional[str]
    f_b = b.get(f_a, "default")  # error: Argument 1 to "get" of "Mapping" has incompatible type "Optional[str]"; expected "str"
