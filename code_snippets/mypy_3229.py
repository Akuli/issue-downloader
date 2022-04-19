def foobar(foo: Union[str, float]):
    if foo in ['fizz', 'buzz']:
        reveal_type(foo)
    else:
        pass
