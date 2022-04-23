from typing import Union

class UserTypeA: ...
class UserTypeB: ...

class A:
    def permissions_for(self, user: UserTypeA) -> bool: ...
    
    @property
    def me(self) -> UserTypeA: ...

class B:
    def permissions_for(self, user: UserTypeB) -> bool: ...
    
    @property
    def me(self) -> UserTypeB: ...


def func(x: Union[A, B]) -> bool:
    return x.permissions_for(x.me)


def func(x: Union[A, B]) -> bool:
    if isinstance(x, A):
        return x.permissions_for(x.me)
    else:
        return x.permissions_for(x.me)
