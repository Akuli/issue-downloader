def less_than(value: int, limit: int | None) -> bool:
    if limit is None:
        return True
    return value < limit

def less_than(value: int, limit: int | Literal[float("inf")]) -> bool:
    return value < limit
