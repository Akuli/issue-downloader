from typing import Type

class Foo:
	def __set_name__(self, owner: Type['Bar'], name: str) -> None:
		...

class Bar:
	foo_bar = Foo() # correctly passes

class Baz:
	foo_baz = Foo() # should fail
