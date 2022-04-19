from mypy_extensions import NamedTupleUnion

class Shape(NamedTupleUnion):  # This would be roughly similar to original union type
    pass

class Circle(Shape):
    radius: float

class Rectangle(Shape):
    width: float
    height: float
