from typing import Union, Dict

class A(object):
    def __init__(self, user: Dict[str, Union[str, bool, list, Dict[str, Union[bool, list]]]]):
        d1 = {
            'a': user['name'],
        }

        d2 = {
            'c': 3,
        }

        self.d3 = {**d1, **d2}

print(A({'name': 'victor'}).d3)
