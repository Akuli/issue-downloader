class C:
    def f(self, x: int) -> None: pass
class D(C):
    def g(self, y: int) -> None: pass
    f = g  # Incompatible types in assignment (expression has type Callable[[Arg('y', int)], None], 
           # base class "C" defined the type as Callable[[Arg('x', int)], None])
