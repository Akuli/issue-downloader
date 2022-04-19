from typing import TypeVar

Self = TypeVar("Self")

    
class A:
    def foo(self: Self) -> Self:
        return self
        
class B(A):
    def foo(self) -> B: # no error
        return B()
        
class C(B):
    a = 1

T = TypeVar("T", bound=A)

def foo(a: T) -> T:
    return a.foo()
    
print(foo(C()).a) # runtime error
