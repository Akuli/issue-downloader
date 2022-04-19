from typing import Protocol, Generic, TypeVar, NamedTuple, List, Any

class Example(Protocol):
    sentence: List[str]

T = TypeVar('T', bound=Example)

class Dataset(Generic[T]):
    ...

class ConcreteExample(NamedTuple):
    sentence: List[str]
    others: Any

class ConcreteDataset(Dataset[ConcreteExample]):
    ...
