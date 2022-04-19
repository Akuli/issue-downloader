from typing import TypeVar, Generic

class T: ...
class M(T): ...
class B(M): ...

InMT = TypeVar('InMT', bound=M)
ContraMT = TypeVar('ContraMT', bound=M, contravariant=True)
CoMT = TypeVar('CoMT', bound=M, covariant=True)

class In(Generic[InMT]):
    x: InMT
class Contra(Generic[ContraMT]):
    x: ContraMT
class Co(Generic[CoMT]):
    x: CoMT

t = T()
m = M()
b = B()

m_in: In[M] = In()
m_contra: Contra[M] = Contra()
m_co: Co[M] = Co()

m_in.x = t  # mypy: Incompatible types in assignment (expression has type "T", variable has type "M").
m_in.x = m
m_in.x = b

m_contra.x = t  # mypy: Incompatible types in assignment (expression has type "T", variable has type "M").
m_contra.x = m
m_contra.x = b

m_co.x = t  # mypy: Incompatible types in assignment (expression has type "T", variable has type "M").
m_co.x = m
m_co.x = b
