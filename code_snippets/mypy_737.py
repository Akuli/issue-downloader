CV = TypeVar('CV', covariant=True)

class A(Generic[CV]):
    def foo(self) -> List[CV]: ...   # Error, should be 
        # Sequence[CV] or similar, since List is invariant
