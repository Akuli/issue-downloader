import random
from typing import (
        Type,
        )


# CASE ONE (works as expected):

str_type_1: Type[str] = str
reveal_type(str_type_1)  # Revealed type is "Type[builtins.str]"


# CASE TWO (unexpected behaviour):

str_type_2: Type[str]
reveal_type(str_type_2)  # Revealed type is "Type[builtins.str]"
str_type_2 = str
reveal_type(str_type_2)  # Revealed type is "<nothing>"


# MISC. INFO that may give insights:

str_type_3: Type[str]
str_type_3 = str_type_2  # no error

# reveal_type(str_type_2) is "<nothing>", yet...
if isinstance(str_type_2, type):
    reveal_type(None)  # generates output; appears to be reachable (correct)
else:
    reveal_type(None)  # no output; not reachable (correct)


# MOTIVATION (a sketch of how this appears in real code):

class StrSubtype(str):
    pass

str_type_4: Type[str]
if random.random() <= 0.50:
    str_type_4 = str
else:
    str_type_4 = StrSubtype

instance: str = str_type_4()  # error: <nothing> not callable  [misc]
