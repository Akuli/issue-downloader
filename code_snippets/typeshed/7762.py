# TODO: Type this more accurately
# Vec2D is actually a custom subclass of 'tuple'.
Vec2D: TypeAlias = tuple[float, float]

# Python 3.10.1; mypy 0.950
from turtle import Vec2D
# Vec2D is a class and a type alias

v1 = Vec2D(1,1) # mypy doesn't recognize it as callable

v2 = v1.rotate(90) # illustrate that Vec2D has methods
