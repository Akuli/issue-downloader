class Circle:
    radius: float

class Rectangle:
    width: float
    height: float

Shape = Union[Circle, Rectangle]

def area(s: Shape) -> float:
    if isinstance(s, Circle):
        result = math.pi * s.radius**2
    elif isinstance(s, Rectangle):
        result = s.width * s.height
    return result

def area(s: Shape) -> float:
    if isinstance(s, Circle):
        result = math.pi * s.radius**2
    elif isinstance(s, Rectangle):
        result = s.width * s.height
    return result   # Error: "result" may be undefined (union item "Triangle" not handled)

from mypy_extensions import NamedTupleUnion

class Shape(NamedTupleUnion):  # This would be roughly similar to original union type
    pass

class Circle(Shape):
    radius: float

class Rectangle(Shape):
    width: float
    height: float
