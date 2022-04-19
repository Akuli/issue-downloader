# All lines are marked precise
from typing import TypedDict

UserDict = TypedDict('UserDict', {'user_id': int, 'email': str})

user:UserDict = { 'user_id': 1, 'email': 'you@somewhere.com' }
