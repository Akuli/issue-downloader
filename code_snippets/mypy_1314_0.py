class C(metaclass=ABCMeta):
    @classmethod
    def foo(cls) -> None: cls().bar()
    @abstractmethod
    def bar(self): raise NotImplementedError
