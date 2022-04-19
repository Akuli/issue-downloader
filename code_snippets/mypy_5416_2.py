from typing import TypeVar, Generic
T = TypeVar('T')
class K(Generic[T]):
	@classmethod
	def m(cls) -> T:
		raise NotImplementedError
