def foo(a: str) -> None:
    ...


# pseudo code
def bar(*args: foo.args, **kwargs: foo.kwargs) -> foo.return_type:
    return foo(*args, **kwargs)
