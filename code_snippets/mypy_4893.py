from typing import cast

import numpy as np # type: ignore

class C: ...

a = cast(C, np.array([1,2,3]))
b: C = np.array([1,2,3])
