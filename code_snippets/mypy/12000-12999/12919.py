from typing import (
    TypeVar, 
    Protocol, Generic, 
    Optional as Opt
)


_T = TypeVar('_T')

class _F(Protocol[_T]):
    def __call__(self, __x: _T) -> _T:
        ...

# Lifting with a function...
def lift(f: _F[_T]) -> _F[Opt[_T]]:
    # This function would do more, but I just return f for the
    # type checking example
    return f # type: ignore

def f(x: int) -> int:
    return x

reveal_type(lift(f))  # _F[Opt[int]] -- as expected

def g(x: _T) -> _T:
    return x

reveal_type(lift(g)) # _F[Union[_T`-1,None]] -- _T is bound (incorrectly?)
                     # pyre thinks this is _F[None] which is also odd...
lift(g)(1)  # so won't accept int

# Moving generic type to Generic...
class lifted(Generic[_T]):
    """Lift type _T to Opt[_T]."""

    def __init__(self, f: _F[_T]) -> None:
        self._f = f

    def __call__(self, x: Opt[_T], /) -> Opt[_T]:
        """Call lifted."""
        return self._f(x) # type: ignore

reveal_type(lifted[_T])  # _F[T?] -> lifted[_T?]

reveal_type(lifted(f))          # lifted[int] -- perfect
reveal_type(lifted(f).__call__) # Opt[int] -> Opt[int] -- perfect
lifted(f)(1)                    # We can call with int
lifted(f)(None)                 # We can call with None

reveal_type(lifted(g))            # lifted[_T`1] -- _T is bound!
                                  # pyre thinks (correctly I think) it is lifted[_T]
reveal_type(lifted(g).__call__)   # Opt[_T`1] -> Opt[_T`1]
                                  # pyre says Any -> Any which I suppose is fine
lifted(g)(1)                      # incompatible type, int isn't an Opt[_T]
                                  # pyre seems to accep this one
lifted(g)(None)                   # but at least None is in Opt[_T]...

reveal_type(lifted[_T](g))          # lifted[_T?] -- Ok
reveal_type(lifted[_T](g).__call__) # def (None) ???
                                    # pyre: Opt[_T] -> Opt[_T] as expected

lifted[_T](g)(1)             # incompatible type "int"; expected "None"
lifted[_T](g)(None)          # but at least None works...
# Pyre doesn't like the [_T] here but accepts the calls without it...
