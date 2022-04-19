import numpy as onp
import numpy.typing as onpt
imin: onpt.NDArray[onp.int64] = onp.array(0)
imax: onpt.NDArray[onp.int64] = onp.array(2)
M = onp.array([1.0, 2.0, 3.0, 4.0])
print(M[imin:imax])
