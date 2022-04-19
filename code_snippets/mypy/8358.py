class Base():
    __slots__: List[str] = ['foo', 'bar']
    if TYPE_CHECKING:
        foo: int
        bar: int

class Derived(Base):
    __slots__: List[str] = ['bar']
