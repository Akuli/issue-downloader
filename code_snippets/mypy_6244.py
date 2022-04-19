from typing import TypeVar, Type
import abc

X = TypeVar("X", bound='Test')

class Test(abc.ABC):
    @abc.abstractclassmethod
    def test(cls: Type[X]) -> X:
        # The erased type of self "Type[t.Test]" is not a supertype of its class "t.Test"
        raise NotImplementedError

    @classmethod
    def test(cls: Type[X]) -> X:  # No error
        pass
