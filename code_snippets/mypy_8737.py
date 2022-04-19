from typing import overload


class Example:

	@overload
	def fun(self, p: int) -> int: ...
	@overload
	def fun(self, p: str) -> str: ...

	def fun(self, p=1):
		if isinstance(p, int):
			return 'foo'
		else:
			return 'bar'

	prop = property(fun)
