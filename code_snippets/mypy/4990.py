from typing import NewType
class C:
    @classmethod
    def foo(cls) -> int: pass
D = NewType('D', C)
D.foo()  # Runtime error here (line 5)
