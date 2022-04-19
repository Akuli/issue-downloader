from abc import ABC, abstractmethod
from typing import List, Type, Dict


class BaseModel(ABC):
    @property
    @classmethod
    @abstractmethod
    def model_code(cls) -> str:
        pass

    # model_code: str


class M1(BaseModel):
    model_code = "m1"


class M2(BaseModel):
    model_code = "m2"


class ModelMapper:
    def __init__(self, model_list: List[Type[BaseModel]]):
        self.__registry: Dict[str, Type[BaseModel]] = {
            mc.model_code: mc for mc in model_list
        }

    def get_model_class(self, model_code: str) -> Type[BaseModel]:
        return self.__registry[model_code]

    def add_model_class(self, model_class: Type[BaseModel]):
        self.__registry[model_class.model_code] = model_class


mm = ModelMapper([M1, M2])
for m in ["m1", "m2"]:
    print("code: ", m, " class: ", mm.get_model_class(m))
