# t.py
class A:
    def __new__(cls, *args, **kwargs) -> "B | C":
        if cls is A:
            cls = B
        else:
            cls = C
        return object.__new__(cls)

class B(A):
    pass

class C(A):
    pass
