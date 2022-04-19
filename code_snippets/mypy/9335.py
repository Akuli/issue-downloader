from typing import TypedDict


class Base(TypedDict):
    id: int


class Derived(Base, total=False):
    description: str


update_me: Derived = {
    'id': 1,
    'description': 'norsetanrst'
}

new_data: Derived = {
    'id': 2
}
# "incompatible type" error from mypy
update_me.update(new_data)
