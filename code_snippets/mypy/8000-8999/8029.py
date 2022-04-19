# mypy: no-implicit-optional

def add(self, a: int, b: int = None) -> int:
    return a + b
