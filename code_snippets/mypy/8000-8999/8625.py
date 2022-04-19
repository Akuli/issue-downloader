from attr import attrs, attrib
from typing import FrozenSet, Text


@attrs
class Test(object):
    values = attrib(type=FrozenSet[Text], converter=frozenset)


Test(values={'a'})
