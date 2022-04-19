class A:
    attr = None


class B(A):
    attr: str  # type: ignore


class C1(B):
    attr = "test"


class C2(B):
    pass


class D(C2):
    attr = "test"
