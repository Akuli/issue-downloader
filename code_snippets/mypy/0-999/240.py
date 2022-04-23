class A:
    def f(self) -> None:
        self.x = 1
A.x = 1 # accepted, but should be an error

class A:
    x = 1
A.x = 1 # ok, and should be ok
