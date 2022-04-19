from typing import TypeGuard


def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

l1: list[object] = []
l2 = l1

if is_str_list(l1):
    l2.append(1)
    impostor: str = l1[0]  # SUS ALERT!!!! 😳😳😳😳😳😳😳
