import arbitrary_module

def f() -> arbitrary_module.MyType:
    x = 1
    y = 2

# reveal_type(arbitrary_module.MyType)
