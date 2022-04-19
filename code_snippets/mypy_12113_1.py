import typing

# This import is required to trigger bug.
import mypybug as eitem

class ClassB(typing.Protocol):
    field: str
