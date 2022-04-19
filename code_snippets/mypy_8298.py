class A:
    def f(self, x: int, y: str, z: float) -> None: pass

class B(A):
    def f(  # Argument 3 incompatible with supertype "A" <-- reported here
            self,
            x: int,
            y: str,
            z: bool,  # <-- would be better to report it here
    ) -> None:
        pass
