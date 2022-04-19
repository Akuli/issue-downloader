from typing import Dict

def foo(x: Dict) -> str:
    result = x.get('foo', None)
    reveal_type(result)  # E: Revealed type is 'Any'
    return result
