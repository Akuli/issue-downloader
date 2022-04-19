d: Dict[str, str] = {}

def foo(arg: Optional[str] = None) -> None:
    if arg is None:
        arg = "foo bar"
    reveal_type(arg)  # str
    print(arg.split())
