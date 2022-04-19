# Code with imprecise lines
from typing import TypedDict

class UserDict(TypedDict):
  user_id: int  # Marked imprecise
  email: str  # Marked imprecise

user:UserDict = { 'user_id': 1, 'email': 'you@somewhere.com' }
