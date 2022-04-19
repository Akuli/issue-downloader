from typing import Literal

class A:
    foo : Literal['bar', 'spam']= 'bar'
    
class B(A):
    foo = 'spam'
