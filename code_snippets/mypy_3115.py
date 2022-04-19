from abc import abstractmethod

class Base:
    @abstractmethod
    def f(self) -> None: pass
class A(Base):
    def f(self) -> None: pass
class B(Base):
    def f(self) -> None: pass

t = [A, B]

t[0]()  # Cannot instantiate abstract class 'Base' with abstract attribute 'f'
