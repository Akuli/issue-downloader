class A:
    def f(self):
        raise NotImplementedError

    def g(self):
        """A is not an abstract base class"""
        return "Hello World"

class B(A):
    def f(self):
        return 5

class C:
    def f(self):
        pass

class A:
    def f(self) -> None: ...
    def g(self): ...

class B(A):
    def f(self): ...

class C:
    def f(self) -> None: ...

class A:
    def f(self): ...
    def g(self): ...

class B(A):
    def f(self): ...

class C:
    def f(self): ...

def h(a: A):
    return a.f()

h(B())

