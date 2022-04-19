from typing import Tuple, Dict, Any


class MyMeta(type):
    def __new__(cls, name: str, bases: Tuple[type, ...], dict: Dict[str, Any]) -> type:
        return type.__new__(name, bases, dict)
