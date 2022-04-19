class A:
    def __init__(self) -> None:
        pass
class B:
    def __init__(self, a: Optional[A]=None, b: Optional['B']=None) -> None:
        self.a=a
        self.b=b


N = TypeVar('N')
class PB(Protocol[N]):
    a: Optional[N]
    b: Optional['PB[N]']

def spam(b: PB[N], a: N):
    pass

spam(B(), A())
