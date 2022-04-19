from typing import Literal, Union
from enum import Enum

class ModelType(str, Enum):
    Simple1 = "simple1"
    Simple2 = "simple2"
    Complex1 = "complex1"
    Complex2 = "complex2"

class BaseModel:
    type: ModelType
    
class BaseSimpleModel(BaseModel):
    type: Literal[ModelType.Simple1, ModelType.Simple2]
    simple: str
    
class Simple1Model(BaseSimpleModel):
    type: Literal[ModelType.Simple1]
    
class Simple2Model(BaseSimpleModel):
    type: Literal[ModelType.Simple2]
    
SimpleModel = Union[Simple1Model, Simple2Model]

class BaseComplexModel(BaseModel):
    type: Literal[ModelType.Complex1, ModelType.Complex2]
    complex: str

class Complex1Model(BaseComplexModel):
    type: Literal[ModelType.Complex1]
    
class Complex2Model(BaseComplexModel):
    type: Literal[ModelType.Complex2]
    
ComplexModel = Union[Complex1Model, Complex2Model]
    
Model = Union[SimpleModel, ComplexModel]


model: Model = Simple1Model()

if model.type == ModelType.Simple1 or model.type == ModelType.Simple2:
    reveal_type(model)
    reveal_type(model.simple)
else:
    reveal_type(model)
    reveal_type(model.complex)
