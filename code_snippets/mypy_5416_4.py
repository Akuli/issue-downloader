from typing import TypeVar, Generic
T = TypeVar('T')
class K(Generic[T]):
	def __init__(self, t: T) -> None:
		self.t = t
