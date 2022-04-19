from typing import Dict, Union

d: Dict[Union[str, int], None] = {}

e: Dict[str, None] = {}

# not ok
d.update(e)

# ok
d.update(e.items())

# ok
for key, value in e.items():
    d[key] = value
