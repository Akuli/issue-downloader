T = TypeVar('T')
TA = TypeVar('TA', bound='A')
TC = TypeVar('TC', bound='C')

class A:
    def f(self: T) -> T: ...  # Should be error
    def g(self: TC) -> TC: ...  # Should be error
    def h(self: TA) -> TA: ...  # OK

class C: pass
