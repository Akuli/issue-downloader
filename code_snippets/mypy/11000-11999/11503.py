import mod
import package

mod.func(package.things.Thing())

def func(it):
    ...

from package.things import Thing

def func(it: Thing) -> None: ...

class Thing:
    ...
