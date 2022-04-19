from typing import Dict, Optional

foo_dict: Dict[str, Optional[str]] = {'bar': 'baz'}

if foo_dict['bar'] is not None:
    foo_dict['bar'] = None
    foo_dict['bar'].upper()
