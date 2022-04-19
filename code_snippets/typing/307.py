class Base: pass
class Derived(Base): pass

T = TypeVar('T', bound=Base)
class MyType(Generic[T]):
    pass

myvar: MyType = None  # type of `myvar` is `MyType[Any]`

class Base: pass
class Derived(Base): pass

T = TypeVar('T', bound=Base, default=Base)
class MyType(Generic[T]):
    pass

myvar: MyType = None  # type of `myvar` is `MyType[Base]`
