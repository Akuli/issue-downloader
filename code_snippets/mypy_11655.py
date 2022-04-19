from typing import TypeVar, Generic
T1, T2 = TypeVar('T1'), TypeVar('T2')

class Container(Generic[T1]):
    class Item(Generic[T2]):
        pass
