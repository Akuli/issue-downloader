from abc import ABCMeta
from typing import Generic, TypeVar, Union


class BaseEngine(metaclass=ABCMeta):
    pass


class BaseEngineVariantA(BaseEngine):
    pass


class BaseEngineVariantB(BaseEngine):
    pass


class VariantAConcreteEngine(BaseEngineVariantA):
    pass


CombinedTypes = Union[BaseEngineVariantA, BaseEngineVariantB]
T = TypeVar('T', bound=CombinedTypes)


class IBase(Generic[T], metaclass=ABCMeta):
    def __init__(self, engine: T):
        self.engine = engine


class IAction(IBase[T], metaclass=ABCMeta):
    pass


class ErrorIfUsingTypeVar(IBase[T]):
    def __init__(self, something: T, actions_injected: type[IAction[T]]) -> None:
        self.something = something
        self.actions_injected = actions_injected

    def foo(self) -> None:
        if not isinstance(self.something, VariantAConcreteEngine):
            raise Exception("HI")

        self.actions_injected(self.something)  # Gives a mypy error of - error: Argument 1 to "IAction" has incompatible type "VariantAConcreteEngine"; expected "T"


class WorksFineUsingUnionsAlone(IBase[CombinedTypes]):
    def __init__(self, something: CombinedTypes, actions_injected: type[IAction[CombinedTypes]]) -> None:
        self.something = something
        self.actions_injected = actions_injected

    def foo(self) -> None:
        if not isinstance(self.something, VariantAConcreteEngine):
            raise Exception("HI")

        self.actions_injected(self.something)  # No error if using unions alone

