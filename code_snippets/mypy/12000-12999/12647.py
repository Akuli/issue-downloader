from random import choice
from typing import Literal, Union


a: Union[Literal[1], Literal[2]]
a = choice([1, 2])  # no error as expected
a = choice((1, 2))  # Argument 1 to "choice" has incompatible type "Tuple[int, int]"; expected "Sequence[Union[Literal[1], Literal[2]]]"  [arg-type]
