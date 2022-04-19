def f(x: Iterable[int]) -> None:
    if not x:  # Might never be taken, or at least this could be inconsistently taken
        print('x')

class A:
    pass  # No __nonzero__

def g(a: A) -> None:
    if not a:   # Similar to above? What if there are subclasses of 'A'?
        print('x')
