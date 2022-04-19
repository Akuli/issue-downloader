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
