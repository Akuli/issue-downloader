from typing import ClassVar, Generic, TypeVar

from Phidget22.Phidget import Phidget as Phidget22PhidgetAPI  # Ignored in config

TKeys = TypeVar("TKeys")

class Base(Phidget22PhidgetAPI, Generic[TKeys]):

    foo: ClassVar[TKeys]

    # If this is not commented out, the bug surfaces
    def __init__(self):
        super().__init__()

reveal_type(Base.foo)

class Child(Base[str]):

    foo: ClassVar[str] = "bar"
    reveal_type(foo)

reveal_type(Child.foo)

