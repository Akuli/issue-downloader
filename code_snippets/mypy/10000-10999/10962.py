from typing import Type

class Base:
    ...

def get_base() -> Type[Base]:
    return Base

BaseAlias: Type[Base] = get_base()

class Derived(BaseAlias):
    ...
