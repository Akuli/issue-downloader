class L:
    a: int

class R:
    b: int

class Both(L, R):
    pass


class A:
    @property
    def x(self) -> L: ...

class B:
    @property
    def x(self) -> R: ...

class C(A, B):  # error: Definition of "i" in base class "A" is incompatible with definition in base class "B"
    pass

both: L = Both()
assert isinstance(both, R)
reveal_type(both)  # Revealed type is "<subclass of "L" and "R">"
c: A = C()
assert isinstance(c, B)  # error: Subclass of "A" and "B" cannot exist: would have incompatible method signatures
reveal_type(c)  # expected "subclass of A and B", actual "A"
reveal_type(c.x)  # expected "subclass of L and R", actual "L"
