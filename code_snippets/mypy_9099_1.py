from typing import List
from typing_extensions import Literal

lit1: Literal[1]
lit2: Literal[2, 3]

arr2 = [lit1, lit2]

reveal_type(arr2)
