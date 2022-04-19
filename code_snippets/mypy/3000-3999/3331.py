from typing import *
SortedList = NewType('SortedList', List)
A = TypeVar('A')
def my_sorted(items: List[A]) -> SortedList[A]:
    ...
