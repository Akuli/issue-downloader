from typing import TypeVar, Generic
T = TypeVar('T', int, str)
class K(Generic[T]):
	@classmethod
	def m(cls) -> T:
		raise NotImplementedError

from typing import TypeVar, Generic
S = TypeVar('S')
T = TypeVar('T', int, str)
class K(Generic[T]):
	@classmethod
	def m(cls: S) -> T:
		raise NotImplementedError

from typing import TypeVar, Generic
T = TypeVar('T')
class K(Generic[T]):
	@classmethod
	def m(cls) -> T:
		raise NotImplementedError

from typing import TypeVar, Generic
T = TypeVar('T', int, str)
class K(Generic[T]):
	def __init__(self, t: T) -> None:
		self.t = t

from typing import TypeVar, Generic
T = TypeVar('T')
class K(Generic[T]):
	def __init__(self, t: T) -> None:
		self.t = t

from typing import TypeVar, Generic
T = TypeVar('T', int, str)
class K(Generic[T]):
	def __init__(self, t: T) -> None:
		self.t: T = t

class L(K[T]):
	def __init__(self, t: T) -> None:
		self.u = 1
		super().__init__(t=t)
