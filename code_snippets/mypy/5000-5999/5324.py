from typing import Generic, TypeVar


class A:
    pass


class B:
    pass


T_Value = TypeVar("T_Value", A, B)


class Guess(Generic[T_Value]):
    def __init__(self, value: T_Value, confidence: float) -> None:
        self.value = value  # <-- line 17
        self.confidence = confidence

class Guess(Generic[T_Value]):
    def __init__(self, value: T_Value, confidence: float) -> None:
        self.value: T_Value = value
        self.confidence = confidence
