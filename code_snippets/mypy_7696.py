from typing import List, Optional, Any

class MyClass1:

    _result: Optional[List[str]] = None
    _foo: Any = None

    @classmethod
    def get(cls, some_arg: Optional[str]) -> List[str]:
        if cls._result is None:
            cls._result = [some_arg or 'a'] + (
                cls._foo.split(',') if cls._foo else []
            )
        return cls._result

class MyClass2:

    _result: Optional[List[str]] = None
    _foo: Any = None

    @classmethod
    def get(cls, some_arg: Optional[str]) -> List[str]:
        if not cls._result:
            cls._result = [some_arg or 'a'] + (
                cls._foo.split(',') if cls._foo else []
            )
        return cls._result
#       ^ [mypy] : Incompatible return value type (got "Optional[List[str]]", expected "List[str]")

