class MySubType(TypedSimpleNamespace):
   bar: int

class MyType(TypedSimpleNamespace):
   foo: MySubType

# correct
a: MyType = SimpleNamespace(foo=SimpleNamespace(bar=1))
# incorrect, `bar` should be a number
a: MyType = SimpleNamespace(foo=SimpleNamespace(bar='abc'))
