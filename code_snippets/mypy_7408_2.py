def f(a: int, b: int) -> None: pass

def g(x: List[int]) -> None:
    assert len(x) == 2
    f(x[0], x[1])
