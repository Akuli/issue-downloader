from typing import Tuple, Optional

a: Tuple[Optional[int], Optional[int]] = (1, 1)
b: Tuple[int, int]
if a[0] is not None and a[1] is not None:
    b = a
