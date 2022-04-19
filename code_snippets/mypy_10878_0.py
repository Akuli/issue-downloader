@overload
def f(x: None, y: None) -> None:...

@overload
def f(x: str, y: int) -> int:...

def f(x: Optional[str], y: Optional[int]) -> Optional[int]:
    if x is not None:
        return len(x) + y # error: Unsupported operand types for + ("int" and "None")
    else:
        return None
