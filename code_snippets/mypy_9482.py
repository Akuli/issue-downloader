# THIS VERSION WORKS, BUT REQUIRES MODIFYING CODE WITH EXTRA CLASS
from typing import TypeVar, Generic, List, Union, overload
from typing_extensions import Protocol
from datetime import datetime

T = TypeVar("T", covariant=True)
S = TypeVar("S")

class datetime64(int):
    """Stand-in for np.datetime64."""


class IndexType(Protocol[T]):
    def first(self) -> T: ...


class Index:

    @overload
    def __new__(cls, values: List[datetime64]) -> "Datetime64Index": ...
    @overload
    def __new__(cls, values: List[datetime]) -> "Datetime64Index": ...
    @overload
    def __new__(cls, values: List[S]) -> "DefaultIndex[S]": ...

    def __new__(cls, values):
        if type(values[0]) in (datetime, datetime64):
            cls = Datetime64Index
        else:
            cls = DefaultIndex
        return object.__new__(cls)


class DefaultIndex(Index, Generic[S]):
    def __init__(self, values: List[S]):
        self.values = values

    def first(self) -> S:
        return self.values[0]


class Datetime64Index(DefaultIndex):

    def __init__(self, values: Union[List[datetime], List[datetime64]]):
        self.values : List[datetime64] = [
            datetime64(o.timestamp()) if isinstance(o, datetime) else o
            for o in values
        ]

    def first(self) -> datetime:
        return datetime.fromtimestamp(self.values[0])


# Should work
a: IndexType[datetime] = Index([datetime64(100)])
b: IndexType[datetime] = Index([datetime(2000, 10, 20)])
c: IndexType[bool] = Index([True])

# Should complain
d: IndexType[datetime] = Index(["a"])
e: IndexType[bool] = Index(["a"])

# THIS VERSION SHOULD WORK, BUT CAUSES MYPY TO ERRONEOUSLY(?) COMPLAIN
from typing import TypeVar, Generic, List, Union, overload
from typing_extensions import Protocol
from datetime import datetime

T = TypeVar("T", covariant=True)
S = TypeVar("S")

class datetime64(int):
    """Stand-in for np.datetime64."""


class IndexType(Protocol[T]):
    def first(self) -> T: ...


class Index(Generic[S]):

    @overload
    def __new__(cls, values: List[datetime64]) -> "Datetime64Index": ...
    @overload
    def __new__(cls, values: List[datetime]) -> "Datetime64Index": ...
    @overload
    def __new__(cls, values: List[S]) -> "Index[S]": ...

    def __new__(cls, values):
        if type(values[0]) in (datetime, datetime64):
            cls = Datetime64Index
        return object.__new__(cls)

    def __init__(self, values: List[S]):
        self.values = values

    def first(self) -> S:
        return self.values[0]


class Datetime64Index(Index):

    def __init__(self, values: Union[List[datetime], List[datetime64]]):
        self.values : List[datetime64] = [
            datetime64(o.timestamp()) if isinstance(o, datetime) else o
            for o in values
        ]

    def first(self) -> datetime:
        return datetime.fromtimestamp(self.values[0])


# Should work
a: IndexType[datetime] = Index([datetime64(100)])
b: IndexType[datetime] = Index([datetime(2000, 10, 20)])
c: IndexType[bool] = Index([True])

# Should complain
d: IndexType[datetime] = Index(["a"])
e: IndexType[bool] = Index(["a"])

