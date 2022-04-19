from typing import Generic, Any, TypeVar, List, Dict, cast, Callable

import dataclasses


MetaDataType = TypeVar('MetaDataType')

@dataclasses.dataclass
class Item(Generic[MetaDataType]):
	value: int
	metadata: MetaDataType


ItemType = TypeVar('ItemType', bound = Item)

# Generic[ItemType[MetaDataType]] fails at runtime, but mypy does not complain about it
class BasicStorage(Generic[ItemType[MetaDataType]]):

	def __init__(self) -> None:
		self._storage: List[ItemType] = []

	def item_factory(self, value: int, metadata: MetaDataType) -> ItemType:
		# This fails without cast altought `ItemType` has upper bound on `Item`
		return cast(ItemType, Item[MetaDataType](value, metadata))

	def get_last_item(self) -> ItemType:
		return self._storage[-1]

	def append(self, value: int, metadata: MetaDataType) -> ItemType:
		item = self.item_factory(value, metadata)
		self._storage.append(item)
		return item


class ExtendedItem(Item[Dict[str, Any]]):
	''' Some helper properties '''


class ExtendedStorage(BasicStorage[ExtendedItem]):

	# Causes error: Argument 2 of "item_factory" is incompatible with supertype "BasicStorage"; supertype defines the argument type as "MetaDataType"
	# Although ExtendedItem is basically `Item[Dict[str, Any]]`
	def item_factory( # type: ignore
		self,
		value: int,
		metadata: Dict[str, Any]
	) -> ExtendedItem:
		return ExtendedItem(value, metadata)
