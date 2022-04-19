from typing import Callable, Optional

class Base:
    formatter1: Callable[[int], str]
    formatter2: Optional[Callable[[int], str]]
    formatter3: Optional[Callable[[int], str]]
    formatter4: Optional[Callable[[int], str]]

class Sub(Base):
    @staticmethod
    def formatter1(value: int) -> str:
        return str(value)
    @staticmethod
    def formatter2(value: int) -> str:
        return str(value)
    formatter3 = formatter2
    formatter4 = str
