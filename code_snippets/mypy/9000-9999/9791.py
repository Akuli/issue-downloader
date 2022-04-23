from typing import Union, Tuple, List

variable: List[Union[Tuple[int, int], Tuple[str, str]]] = []

element1 = variable[0]

print(element1[0] + element1[1])
