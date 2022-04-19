class C: pass
class B(C): pass
class A(B): pass

T = TypeVar('T', bound=C)
def factory(cls: Type[T]) -> T:
    return cls()
