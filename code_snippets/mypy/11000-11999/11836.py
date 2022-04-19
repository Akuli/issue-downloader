# t.py
from typing import Tuple, List

ElementT = Tuple[str, Tuple[str, List[str]]]
ContainerT = Tuple[ElementT, ...]

a: ContainerT = tuple((f1, (f2, [])) for f1, f2 in (("", ""), ("", "")))

b: ContainerT = (("", ("", [])),)

# The following four lines should be equally valid (or invalid) regarding types
# but only the last one raises an error
c1: ContainerT = a + b  # works fine !
c2: ContainerT = b + a  # this too !
c3: ContainerT = a + (("", ("", [])),)  # also works
c4: ContainerT = (("", ("", [])),) + a  # but this doesn't
