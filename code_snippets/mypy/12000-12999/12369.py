from typing import Any

print(reveal_type(int | Any))  #  types.UnionType

from typing import Any

isinstance(1, str | Any)  # no error
