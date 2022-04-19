from typing import TypeVar, Generic
S = TypeVar('S')
T = TypeVar('T', int, str)
class K(Generic[T]):
	@classmethod
	def m(cls: S) -> T:
		raise NotImplementedError
