from typing import Dict
from typing_extensions import Literal

T = Literal[1, 2, 3]
d: Dict[T, None]

d = {x: None for x in [1, 2, 3]}
# error: Key expression in dictionary comprehension has incompatible type "int"; expected type "Union[Literal[1], Literal[2], Literal[3]]"

d = dict(zip([1, 2, 3], [None, None, None]))  # no error
d = dict.fromkeys([1, 2, 3])  # no error
