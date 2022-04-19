from typing import TypedDict


class Value(TypedDict):
    key1: str
    key2: str


const1: Value = {"key1": "foo", "key2": "bar"}
const2: Value = {**const1, "key2": "eggs"}
#                ^^^^^^^^
# mypy: Expected TypedDict key to be string literal (10:20)
