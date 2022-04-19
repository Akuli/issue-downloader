import inspect

foo = lambda: None
foo.__signature__ = inspect.signature(foo)
