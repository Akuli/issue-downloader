import typing as t

constructor: t.Type[t.FrozenSet]
reveal_type(constructor)
constructor = frozenset
reveal_type(constructor)
constructor(range(10))
