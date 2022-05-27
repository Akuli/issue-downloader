from .. import b

class Object():
    pass

class ObjectFactory:
    def make_object(self) -> Object:
        pass

OBJECT_FACTORY = ObjectFactory()

from __future__ import annotations
from . import my_directory

def func(bar: Bar):
    print(bar.object)

class Bar:
    def __init__( 
        self,
        _: str, # if you delete this type annotation there will no longer be an error
    ):
        self.object = my_directory.OBJECT_FACTORY.make_object()
