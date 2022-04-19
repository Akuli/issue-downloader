class AddingAccumulatorParam(Generic[U]):
    def addInPlace(self, value1: U, value2: U) -> U:
        return reveal_type(value1.__iadd__(value2))
