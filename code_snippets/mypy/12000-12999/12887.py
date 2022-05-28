from typing import Generic, TypeVar

NumericT = TypeVar('NumericT', int, float)


class BaseThing(Generic[NumericT]):
    def put(self, x: NumericT):
        val = x + 'wrong'    # ERROR:  good, this is expected. 


class IntThing(BaseThing[int]):
    pass


class FloatThing(BaseThing[float]):
    pass


class StringThing(BaseThing[str]):   # ERROR:  good, this is expected. 
    pass


def get() -> BaseThing:
    pass


thing = get()

thing.put('wrong')    # NO ERROR:  this should be an error

if isinstance(thing, IntThing):
    thing.put(2)

from typing import Generic, TypeVar, Union

NumericT = TypeVar('NumericT', int, float, Union[int, float])


class BaseThing(Generic[NumericT]):
    def put(self, x: NumericT):
        val = x + 'wrong'


class IntThing(BaseThing[int]):
    pass


class FloatThing(BaseThing[float]):
    pass


def get() -> BaseThing[Union[int, float]]:
    pass


thing = get()
thing.put('wrong')

if isinstance(thing, IntThing):
    thing.put(2)    # ERROR: <nothing> has no attribute "put"
