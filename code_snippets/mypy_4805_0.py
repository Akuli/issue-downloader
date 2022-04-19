from typing import Dict, Optional

d: Dict[str, str] = {}

def foo(arg: Optional[str] = None) -> None:
    if arg is None:
        arg = d.get("a", "foo bar")
    print(arg.split())
