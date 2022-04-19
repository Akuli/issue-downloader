from typing import Any

def get_any() -> Any:
    return {}

def fun(message_json) -> int:
    messages = [3] # <=== only this line changes
    messages = get_any()
    if not isinstance(messages, list):
        print(messages)
    return 2

