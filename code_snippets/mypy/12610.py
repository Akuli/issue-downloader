from typing import Dict
from typing import Generic
from typing import List
from typing import Tuple
from typing import TypeVar
from typing import Union


class Thing:
    pass


_THING = TypeVar("_THING", bound="Thing")


class ThingCollection(Generic[_THING]):
    _collection: List[Tuple[str, _THING]]

    _index: Dict[Union[None, str, int], _THING]

    def __init__(self, t: _THING):
        self._collection = [("x", t)]
        self._index = {}

    def do_thing(self) -> None:
        self._index.update(
            (idx, c) for idx, (k, c) in enumerate(self._collection)
        )

    def do_thing_workaround(self) -> None:
        self._index.update(
            (idx, c) for idx, c in enumerate(c for (k, c) in self._collection)
        )
