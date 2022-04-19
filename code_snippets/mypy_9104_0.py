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
