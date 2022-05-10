import abc

class A:
    @abc.abstractclassmethod
    def foo(self) -> int:
        return 1

class B(A):
    def foo(self) -> int:
        return 2
