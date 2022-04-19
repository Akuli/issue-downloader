def is_c_function(obj: object) -> bool:
    return inspect.isbuiltin(obj) or type(obj) is type(ord)
