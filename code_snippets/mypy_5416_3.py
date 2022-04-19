from typing import TypeVar, Generic
T = TypeVar('T', int, str)
class K(Generic[T]):
	def __init__(self, t: T) -> None:
		self.t = t
