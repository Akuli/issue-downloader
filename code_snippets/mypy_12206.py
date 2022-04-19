def f(*, x: int = 9, y:int = 8) -> None:
    pass

kwargs = {"x": 1, "y": 2}
f(*kwargs)
