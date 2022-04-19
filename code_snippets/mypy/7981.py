from typing_extensions import final, TypedDict

@final
class Point(TypedDict):
    x: float
    y: float
    z: float


p: Point
x: str
reveal_type(p.values())
reveal_type(p.items())
reveal_type(p.get(x, 0.0))

