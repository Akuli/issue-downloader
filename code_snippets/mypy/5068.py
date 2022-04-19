from typing import Tuple
def test_1(inp1: Tuple[int, int, int]) -> None:
    pass

def test_2(inp2: Tuple[int, int, int]) -> None:
    test_tuple = tuple(e for e in inp2)
    reveal_type(test_tuple)
    test_1(test_tuple)
