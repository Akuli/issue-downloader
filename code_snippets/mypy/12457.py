from typing import Optional, Dict

def test(arg: str) -> None:
    ...

def this_fails(arg: Dict[str, Optional[str]]) -> None:
    if arg.get("key") is not None:
       test(arg["key"])  # error

def this_fails_also(arg: Dict[str, Optional[str]]) -> None:
    if arg.get("key") is not None:
       test(arg.get("key"))  # error

def but_this_pass(arg: Dict[str, Optional[str]]) -> None:
    if arg.get("key") and arg["key"] is not None:
        test(arg["key"])

def this_pass_also_but_is_unsafe(arg: Dict[str, Optional[str]]) -> None:
    if arg["key"] is not None:
        test(arg["key"])

