class A:
    def foo(self) -> int: pass

class B(A):
    def foo(self) -> str: pass  # type: ignore[override]

class C(B):
    def foo(self) -> str: pass
