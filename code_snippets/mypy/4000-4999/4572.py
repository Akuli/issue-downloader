class Immutable:
    def __setattr__(self, attr: str, val: Any) -> NoReturn:
        raise AttributeError("Not with this class!")

class C(Immutable):
    def __init__(self, val: int) -> None:
        object.__setattr__(self, 'val', val)

c = C(42)
if random() < 0.001:
    c.val = 0  # Ideally mypy should say 'Class "C" is frozen' or similar
