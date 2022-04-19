from typing import Dict

def foo(x:Dict) -> str:
    result = x.get('foo')
    reveal_type(result)  # E: Revealed type is 'Union[Any, builtins.None]'
    return result  # E: Incompatible return value type (got "Optional[Any]", expected "str")
