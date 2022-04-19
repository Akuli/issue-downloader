from typing import *

CanCompare = TypeVar("CanCompare", bound='Comparable')


class Comparable(Protocol):
    def __lt__(self: CanCompare, other: CanCompare) -> bool:
        pass

    def __gt__(self: CanCompare, other: CanCompare) -> bool:
        pass

    def __le__(self: CanCompare, other: CanCompare) -> bool:
        pass

    def __ge__(self: CanCompare, other: CanCompare) -> bool:
        pass


A = TypeVar('A', covariant=True)


class CustomList(list, Generic[A]):

    def getMax(self: 'CustomList'[CanCompare]) -> Optional[CanCompare]:
        return functionGetMax(self)


def functionGetMax(aList: 'CustomList'[CanCompare]) -> Optional[CanCompare]:
    pass


canCompareMe: CustomList[int] = CustomList([1, 2, 3])
canCompareMe.getMax()  # ok
functionGetMax(canCompareMe)  # ok


class NotComparable:
    pass  # no comparisons implemented


impossibleToCompare: CustomList[NotComparable] = CustomList([NotComparable(), NotComparable()])
impossibleToCompare.getMax() # Bug: No error raised
functionGetMax(impossibleToCompare)  # Correctly raised error: Value of type variable "CanCompare" of "functionGetMax" cannot be "NotComparable"

