from typing import List, Optional


def example(data: Optional[List[int]] = None, size: int = 0) -> None:
    buffer = bytearray(data if data else size)
    print(buffer)


example(size=3)
example(data=[1, 2, 3])
