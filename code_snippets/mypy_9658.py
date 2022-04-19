def example_1(p1: Optional[int]):
    if p1 is not None:
        late_p1 = (lambda: p1)
        reveal_type(late_p1)

def example_2(p1: Optional[int]):
    if p1 is not None:
        late_p1: Callable[[], int] = (lambda: p1)
        reveal_type(late_p1)

def example_3(p1: Optional[int]):
    if p1 is not None:
        late_p1 = (lambda: p1)
    p1 = None
    inc = late_p1() + 1 # This will crash, but MyPy is perfectly confident that `late_p1()` is an integer.

