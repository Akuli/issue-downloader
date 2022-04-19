def downcast(type, expr):
    assert isinstance(expr, type)
    return expr

x = downcast(type, expr)

assert isinstance(expr, type)
x = expr

def upcast(type, expr):
    return expr

x = upcast(type, expr)

x: type = expr
