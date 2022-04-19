import typing as typ

T = typ.TypeVar('T')

def identity(x:T)->T:
    return x 

A = typ.TypeVar('A')
B = typ.TypeVar('B')
C = typ.TypeVar('C')

def compose_and_apply(x : A
                     ,f : typ.Callable[[A],B]  = identity
                     ,g : typ.Callable[[B],C]  = identity
                     ) -> C:
    return g(f(x))
