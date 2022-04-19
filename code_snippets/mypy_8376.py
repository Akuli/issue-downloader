from typing import Dict, Any, NamedTuple

def out() -> str:
    return "out"

d = {"x": 0, "y": 1}

class Test(NamedTuple):
    qwer: Dict[str, Any] = {k: v for k, v in d}

from typing import Dict, Any, NamedTuple


d = {"x": 0, "y": 1}


class Test(NamedTuple):
    qwer: Dict[str, Any] = {k: v for k, v in d}

