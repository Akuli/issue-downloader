from typing import Iterable, Container, Union

i: Iterable[str]
c: Container[str]
u: Union[Iterable[str], Container[str]]

'x' in i
'x' in c
'x' in u  # Unsupported right operand type for in ("Union[Iterable[str], Container[str]]")
