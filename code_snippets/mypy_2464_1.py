def area(s: Shape) -> float:
    if isinstance(s, Circle):
        result = math.pi * s.radius**2
    elif isinstance(s, Rectangle):
        result = s.width * s.height
    return result   # Error: "result" may be undefined (union item "Triangle" not handled)
