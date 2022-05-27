# ctx.py

from contextlib import ExitStack

class Thing(ExitStack):
    def foo(self) -> None:
        print("foo")

stack = ExitStack()
thing = stack.enter_context(Thing())
reveal_type(thing)
thing.foo()
