def some_function(x): ...
some_function.some_attribute = 42

class FunctionForAdmin(Callable[[], Any]):
    short_description: str
    boolean: bool = False
    admin_order_field: str
    empty_value_display: str

some_function: FunctionForAdmin
def some_function():
    return ...
some_function.short_description = "What a nice little function!"

