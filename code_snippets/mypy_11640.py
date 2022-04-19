import numpy as onp
import numpy.typing as onpt
imin: onpt.NDArray[onp.int64] = onp.array(0)
imax: onpt.NDArray[onp.int64] = onp.array(2)
M = onp.array([1.0, 2.0, 3.0, 4.0])
print(M[imin:imax])

import numpy as onp
import numpy.typing as onpt
imin: onpt.NDArray[onp.int64] = onp.array(0)
imax: onpt.NDArray[onp.int64] = onp.array(2)
M = onp.array([1.0, 2.0, 3.0, 4.0])
islice = slice(imin, imax)
print(M[islice])

[tool.mypy]
plugins = "numpy.typing.mypy_plugin"
check_untyped_defs = true
disallow_any_generics = true
ignore_missing_imports = true
no_implicit_optional = true
show_error_codes = true
strict_equality = true
warn_redundant_casts = true
warn_return_any = true
warn_unreachable = true
warn_unused_configs = true
no_implicit_reexport = false

