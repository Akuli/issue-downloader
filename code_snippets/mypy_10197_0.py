class A:
    def foo(self, s: str) -> str: ...

class B(A):
    def foo(self, n: float) -> float: ... # type: ignore

class C(B):
    def foo(self, n: float) -> float: ...
