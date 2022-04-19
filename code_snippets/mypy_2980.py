class A:
    a: Optional[int]
    b: Optional[int]
    ...
    def f(self) -> None:
        if None in (self.a, self.b):
            return
        print(self.a + self.b)  # ok at runtime but mypy error currently
