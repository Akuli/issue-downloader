# foo.py
class Foo:
    ...

# bar.py
from foo import Foo

# baz.py
from bar import Foo # Module "bar" does not explicitly export attribute "Foo"; implicit reexport disabled  [attr-defined]

reveal_type(Foo) # Revealed type is "Any"
