class C:
    def f(self) -> None:
        self.x: D = D()  # Expression has type "D", variable has type "int"
        self.x: int
        class D: pass

reveal_type(C().x)  # int
