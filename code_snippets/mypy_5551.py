from typing import TypeVar, Generic

class C(Generic[T]):
    def __init__(self, t: T) -> None:
        self.t = t

    class F(Generic[K]):
        def __init__(self, k: K) -> None:
            self.k = k

        def foo(self) -> K:
            return self.k

C.F(17).foo()
C("").F(17).foo()  # error: Argument 1 to "F" has incompatible type "int"; expected "str"

reveal_type(C.F)  # 'def [K] (k: K`1) -> foo.C.F[K`1]'  All Good
reveal_type(C("").F)  # 'def [K] (k: builtins.str*) -> foo.C.F[builtins.str*]'   What?
