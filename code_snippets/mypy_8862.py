def foo(option: bool = None, **kwargs):
    pass

def bar(option: str = '', **kwargs):
    pass


d = {'test': True}

foo(**{'test': True})
foo(**d)
foo(other_option=True, option=True, **d)
foo(option=True, **{'test': True})

bar(**{'test': True})  # Error
bar(**d)  # Error
bar(other_option=True, **d)  # Error
bar(option='Hello, world!', **{'test': True})
