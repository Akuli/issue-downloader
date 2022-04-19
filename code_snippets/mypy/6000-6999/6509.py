from typing import Dict, Generic, TypeVar

Key = TypeVar('Key')

class A(Generic[Key]):
    @staticmethod
    def lookup(d: Dict[Key, int], key: Key) -> None:
        x = d.get(key, 0) + 1

x = 1 + "a"
