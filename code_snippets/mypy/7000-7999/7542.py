f: Any

class MyClass:
    def __init__(*args, **kwargs) -> None: ...
    @classmethod
    def run(self, unicodeaction: str) -> None: ...
    def __reduce__() -> Any: ...
    def __setstate__(state) -> Any: ...

def is_c_function(obj: object) -> bool:
    return inspect.isbuiltin(obj) or type(obj) is type(ord)
