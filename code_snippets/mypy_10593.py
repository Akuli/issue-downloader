from typing import Any, Dict, List, TypedDict, TypeVar, Type, TYPE_CHECKING

class User(TypedDict):
    id: int
    name: str

users: List[Dict[str, Any]] = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

T = TypeVar("T")

def try_cast(cls: Type[T], data: Any) -> T:
    return cls(**data)  # type: ignore

for user in users:
    user_unannotated = try_cast(User, user)
    user_annotated: User = try_cast(User, user)  # Incompatible types in assignment (expression has type "User", variable has type "User")

    if TYPE_CHECKING:
        reveal_type(try_cast)  # def [T] (cls: Type[T`-1], data: Any) -> T`-1
        reveal_type(try_cast(User, {}))  # typed.User*
        reveal_type(user)  # builtins.dict*[builtins.str, Any]
        reveal_type(user_unannotated)  # typed.User*
        reveal_type(user_unannotated["id"])  # builtins.object*
        reveal_type(user_annotated)  # TypedDict('typed.User', {'id': builtins.int, 'name': builtins.str})
        reveal_type(user_annotated["id"])  # builtins.int
