def foo(a: str):
    pass


d = {'key': 'a'}
foo(d.get('key', None) or '26')
