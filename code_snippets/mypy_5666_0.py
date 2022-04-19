from abc import ABC, abstractmethod
from typing import Generic, TypeVar

_InputType = TypeVar('_InputType', contravariant=True)
_IntermediateType = TypeVar('_IntermediateType')
_OutputType = TypeVar('_OutputType', covariant=True)


class GenericBase(Generic[_InputType, _IntermediateType, _OutputType], ABC):
    @abstractmethod
    def first_step(self, pipeline_input: _InputType) -> _IntermediateType: ...

    def second_step(self, state: _IntermediateType) -> _OutputType:
        # By default, pass through state unmodified
        return state

    def execute(self, pipeline_input: _InputType) -> _OutputType:
        state = self.first_step(pipeline_input)
        return self.second_step(state)


class GenericImpl(GenericBase[str, int, float]):
    def first_step(self, pipeline_input: str) -> int:
        return len(pipeline_input)

    def second_step(self, state: int) -> float:
        return state * 1.5


a = GenericImpl()
print(a.execute("aaa"))
