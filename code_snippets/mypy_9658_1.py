def example_2(p1: Optional[int]):
    if p1 is not None:
        late_p1: Callable[[], int] = (lambda: p1)
        reveal_type(late_p1)
