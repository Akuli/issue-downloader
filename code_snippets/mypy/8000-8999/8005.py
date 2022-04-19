from typing import Protocol

class P(Protocol):
    def foo(self) -> int: ...

class A(P):  # mypy does not flag this
    pass

class B:
    pass

test: P = A()  # mypy does not flag this
test = B()  # mypy flags this

print(A().foo() + 5)  # both error at runtime
print(B().foo() + 5)
