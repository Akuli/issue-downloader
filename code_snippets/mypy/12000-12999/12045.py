class Book(models.Model):
    author = models.ForeignKey(Author, null=True)

# related_field_minimal.pyi
from typing import Generic, Literal, Optional, Type, TypeVar, overload

class Model: ...

_M = TypeVar("_M", bound=Optional[Model])

class ForeignKey(Generic[_M]):
    @overload
    def __new__(
        cls,
        to: Type[_M],
        null: Literal[False] = ...,
    ) -> ForeignKey[_M]: ...
    @overload
    def __new__(
        cls,
        to: Type[_M],
        null: Literal[True],
    ) -> ForeignKey[Optional[_M]]: ...
    def __init__(self, to: Type[_M], null: bool) -> None: ...

# models.py
from typing import Optional
from related_field_minimal import ForeignKey, Model


class Test(Model):
    pass


class BookModel(Model):
    required_field = ForeignKey(to=Test, null=False)
    optional_f1 = ForeignKey(to=Test, null=True)
    optional_f2 = ForeignKey[Test](to=Test, null=True)
    optional_f3 = ForeignKey[Optional[Test]](to=Test, null=True)

reveal_type(BookModel.required_field)
reveal_type(BookModel.optional_f1)
reveal_type(BookModel.optional_f2)
reveal_type(BookModel.optional_f3)
