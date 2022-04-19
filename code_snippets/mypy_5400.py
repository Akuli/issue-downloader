from typing import Sequence

def process_elems(elems: Sequence[float]):
    for elem in elems:
        pass
    assert isinstance(elem, int)
    elems_odd = [elem & 1 for elem in elems]
