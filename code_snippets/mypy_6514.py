from typing import Generic, TypeVar, overload, Any, Union
import datetime as dt

T = TypeVar('T')

class Column(Generic[T]):
    @overload
    def __get__(self, instance: None, owner: Any) -> "Column[T]": ...
    @overload
    def __get__(self, instance: object, owner: Any) -> T: ...

    def __get__(self, instance: Union[None, object], owner: Any) -> "Union[Column[T], T]": ...

class MyClass:
    prop: Column[dt.date] = Column()

reveal_type(MyClass.prop)
reveal_type(MyClass().prop)

[mypy]
python_version = 3.6
#show_none_errors = False

