from __future__ import annotations
import numpy as np

class my_float:

    def __radd__(self, other: np.float32) -> my_float:
        return my_float()
