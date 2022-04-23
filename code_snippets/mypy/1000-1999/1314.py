class C(metaclass=ABCMeta):
    @classmethod
    def foo(cls) -> None: cls().bar()
    @abstractmethod
    def bar(self): raise NotImplementedError

C.foo()  # not cool

class D(C):
    def bar(self): pass
D.foo()  # this is fine
