class A: ...

b = 3.0
c = b / len(A())
reveal_type(c)

class A:
    def __len__(self) -> int: return 0

b = 3.0
c = b / len(A())
reveal_type(c)
