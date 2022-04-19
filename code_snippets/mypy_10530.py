from typing import Any, Dict

foo: Dict[str, str]
bar: Dict[Any, int] = {}
foo = bar  # Incompatible types in assignment (expected, correct)
foo = dict(bar)  # no error (unexpected, IMO incorrect)
