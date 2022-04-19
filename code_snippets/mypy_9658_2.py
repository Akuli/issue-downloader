def example_3(p1: Optional[int]):
    if p1 is not None:
        late_p1 = (lambda: p1)
    p1 = None
    inc = late_p1() + 1 # This will crash, but MyPy is perfectly confident that `late_p1()` is an integer.
