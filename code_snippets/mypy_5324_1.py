class Guess(Generic[T_Value]):
    def __init__(self, value: T_Value, confidence: float) -> None:
        self.value: T_Value = value
        self.confidence = confidence
