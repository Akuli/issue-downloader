from typing import List

def f(x: List[int]) -> None:
    assert 'foo' not in x  # Error, but should this be okay?
    ...
