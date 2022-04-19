from typing import Any

def get_any() -> Any:
    return {}

def fun(message_json) -> int:
    messages = [get_any()]
    messages = get_any()
    if not isinstance(messages, list):
        print(messages)
    return 2
