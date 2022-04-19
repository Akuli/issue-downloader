# cython: language_level=3
import cython
from cython import double, size_t
import numpy as np


@cython.boundscheck(False)
def func_with_mv(a: double[:]) -> np.ndarray:
    b: double[:] = np.empty_like(a)
    i: size_t 
    for i in range(len(a)):
        b[i] = 2 * a[i]
    return np.asarray(b)
