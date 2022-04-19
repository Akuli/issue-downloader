def foo(key: str) -> str:
	return key


class A:
	@staticmethod
	def foobar(key: str) -> str:
		return "hello world"


class B(A):
	foobar = staticmethod(foo)
