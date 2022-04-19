from typing import Optional, Set

class Foo:
    pass

bar: Set[Optional[Foo]] = set()
baz: Set[Foo] = bar - {None}
# Incompatible types in assignment (expression has type "Set[Optional[Foo]]",
# variable has type "Set[Foo]")
