def a(x: str) -> str:
    return x

b: int = a('1') # Obviously mypy should raise something here
