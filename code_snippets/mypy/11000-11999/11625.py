from typing import Iterable, Dict, Any


def f(x: Iterable[Dict[str, str]]) -> None:
    pass


# Lists all work as expected
f([])
f([{}])
f([{"k": "v"}])

# Empty tuple works
f(())

# Tuple of empty dict doesn't work
f(({},))

# Tuple with non-empty dict works
f(({"k": "v"},))


f(({},))
