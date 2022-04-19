from typing import Union

list1 = [1, 'b']
list2 = [2, 'd']
list3: list[Union[str, int]] = list1 + list2

dict1 = {1: 'a', 'b': 2}
dict2 = {3: 'c', 'd': 4}
dict3: dict[Union[str, int], Union[str, int]] = dict1 | dict2
