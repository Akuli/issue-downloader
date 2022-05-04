from typing import *

a: Final = 1
reveal_type(a)  # Literal[1]?
reveal_type(1)  # Literal[1]?
