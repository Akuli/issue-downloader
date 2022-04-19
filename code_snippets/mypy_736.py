IV = TypeVar('IV')
CV = TypeVar('CV', covariant=True)

class A(Generic[IV]): ... # Bunch of methods
class B(A[CV], Generic[CV]): pass  # Error, type variable should be invariant
