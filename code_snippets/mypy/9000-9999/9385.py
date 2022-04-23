from typing import List, AnyStr
from glob import glob
import itertools as it
def expand_patterns(
        pats: List[AnyStr],
        sort=True
):
    paths = it.chain(map(glob, pats))
    # Argument 1 to "map" has incompatible type "Callable[[AnyStr, DefaultNamedArg(bool, 'recursive')], List[AnyStr]]"; expected "Callable[[AnyStr], List[AnyStr]]"
    if sort:
        paths = sorted(paths)
    return paths

# Argument 1 to "map" has incompatible type "Callable[[AnyStr, DefaultNamedArg(bool, 'recursive')], List[AnyStr]]"; expected "Callable[[AnyStr], List[AnyStr]]"
