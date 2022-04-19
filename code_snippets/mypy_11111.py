from typing import TypeVar


def handle_str(arg: str) -> str:
    return arg


def handle_list(arg: list) -> list:
    return arg


type_arg = TypeVar('type_arg', str, list[str])


def chooser__standard(arg: type_arg) -> type_arg:
    if isinstance(arg, str):
        return handle_str(arg)
    else:
        return handle_list(arg)


def chooser__ternary(arg: type_arg) -> type_arg:
    return handle_str(arg) if isinstance(arg, str) else handle_list(arg)
