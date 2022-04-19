import dataclasses
import typing

if typing.TYPE_CHECKING:
    import classb as b
    
ItemType = typing.TypeVar('ItemType', bound='b.ClassB')

class Item(typing.Protocol):
    name: str

class ItemBase(typing.Generic[ItemType]):
    pass

# dataclasses required to trigger bug.
@dataclasses.dataclass(kw_only=True)
class ItemBaseX(ItemBase[ItemType]):
    name: str
