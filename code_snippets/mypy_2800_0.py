class C:
    def f(self, x: int) -> None: pass
class D(C):
    def g(self, y: object) -> None: pass
    f = g  # Incompatible types in assignment (expression has type Callable[[object], None], 
           # base class "C" defined the type as Callable[[int], None])
