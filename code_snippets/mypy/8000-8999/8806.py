from typing import TypeVar, Generic, Union

class A:
    pass

class ASub(A):
    pass

class B:
    pass

# Case 1... Success: no issues found
# T_co = TypeVar("T_co", covariant=True)

# Case 2... error: Value of type variable "T_co" of "SomeGeneric" cannot be "ASub"  [type-var]
T_co = TypeVar("T_co", A, B, covariant=True)

# Case 3... Success: no issues found
# T_co = TypeVar("T_co", bound=Union[A, B], covariant=True)


class SomeGeneric(Generic[T_co]):
    pass

class SomeGenericASub(SomeGeneric[ASub]):
    pass

