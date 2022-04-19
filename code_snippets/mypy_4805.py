from typing import Dict, Optional

d: Dict[str, str] = {}

def foo(arg: Optional[str] = None) -> None:
    if arg is None:
        arg = d.get("a", "foo bar")
    print(arg.split())

d: Dict[str, str] = {}

a: str = d.get("a", "a")

d: Dict[str, str] = {}

def foo(arg: Optional[str] = None) -> None:
    if arg is None:
        arg = "foo bar"
    reveal_type(arg)  # str
    print(arg.split())

