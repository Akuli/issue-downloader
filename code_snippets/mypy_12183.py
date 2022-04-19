from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar


import pandas as pd

_DataFrameBound = TypeVar("_DataFrameBound", bound=pd.DataFrame, covariant=True)


class _Method(Protocol[_DataFrameBound]):
    def __call__(self, dataframe: pd.DataFrame) -> _DataFrameBound:
        ...

@dataclass
class MyClass(Generic[_DataFrameBound]):
    _method: _Method[_DataFrameBound]

@dataclass
class MyClassDataFrame(MyClass[pd.DataFrame]):
    ...

def function(dataframe: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

my_class = MyClassDataFrame(function)
