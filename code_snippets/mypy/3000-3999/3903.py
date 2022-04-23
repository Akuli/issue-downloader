Any
class A:
    def foo(self, a: str) -> None: pass


class B(A):
    def foo(self, a):
        reveal_type(a)

Any
str