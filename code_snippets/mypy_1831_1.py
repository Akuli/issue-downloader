class A:
    ...
    @classmethod
    def f(cls: Type[[int], A]) -> A:
        return cls(1)  # ok
