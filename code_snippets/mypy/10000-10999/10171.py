from typing import Dict
a: Dict[int, str] = {}
b: Dict[object, str] = {object(): 'a', 'lol': 'b', **a}
