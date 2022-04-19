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
