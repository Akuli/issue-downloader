from typing import List, Optional

my_list: List[Optional[float]] = []

if my_list[0] is not None:
    result_1: float = my_list[0]        # no error
    result_2: float = my_list[1]        # error: Incompatible types in assignment (expression has type "Optional[float]", variable has type "float")

id_0 = 0
if my_list[id_0] is not None:
    result_3: float = my_list[id_0]     # error: Incompatible types in assignment (expression has type "Optional[float]", variable has type "float")


for i in range(10):
    if my_list[i] is not None:
        a: float = my_list[i]           # error: Incompatible types in assignment (expression has type "Optional[float]", variable has type "float")
