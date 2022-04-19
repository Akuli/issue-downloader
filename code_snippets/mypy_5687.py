from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

_InputType = TypeVar('_InputType', contravariant=True)
_IntermediateType = TypeVar('_IntermediateType')
_OutputType = TypeVar('_OutputType', covariant=True)


class GenericBase(Generic[_InputType, _IntermediateType, _OutputType], ABC):
    @abstractmethod
    def first_step(self, pipeline_input: _InputType) -> _IntermediateType: ...

    def second_step(self, state: _IntermediateType) -> _OutputType:
        # By default, pass through state unmodified
        return cast(_OutputType, state)

    def execute(self, pipeline_input: _InputType) -> _OutputType:
        state = self.first_step(pipeline_input)
        return self.second_step(state)
