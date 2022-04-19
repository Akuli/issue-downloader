from dataclasses import dataclass
import dataclasses
from typing import Any, Dict, Generic, List, Type, TypeVar, Union
from abc import ABC, abstractclassmethod

from occupier.utils import EnhancedJSONEncoder

T = TypeVar("T", bound="DictDataClass")


@dataclass(frozen=True)
class DictDataClass(Generic[T]):
    urn: int

    def to_dict(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls: Type[T], dict_: Dict[str, Any]) -> T:
        return cls(**dict_)

    @classmethod
    def field_names(cls) -> List[str]:
        return [field.name for field in dataclasses.fields(cls)]


@dataclass(frozen=True)
class JSONDataClass(ABC, DictDataClass):

    _JSON_ENCODER = EnhancedJSONEncoder()

    def to_json(self) -> str:
        return JSONDataClass._JSON_ENCODER.encode(self)

    @classmethod
    @abstractclassmethod
    def from_json(cls: Type[T], json_str: str) -> Union[List[T], T]:
        pass

