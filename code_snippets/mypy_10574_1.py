def bar(*args: ParamSpec[foo].args, **kwargs: ParamSpec[foo].kwargs) -> None:
    return foo(*args, **kwargs)
