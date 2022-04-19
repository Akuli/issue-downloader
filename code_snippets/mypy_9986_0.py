from dataclasses import dataclass

@dataclass(order=True)
class Dummy:
    foo: str
    bar: int
