from typing import Union

def semver_prerelease_compare(lhs: str, rhs: str) -> bool:
    a: Union[str, int]
    b: Union[str, int]
    for a, b in zip(lhs.split("."), rhs.split(".")):
        try:
            a = int(a)
        except ValueError:
            pass
        try:
            b = int(b)
        except ValueError:
            pass

        if isinstance(a, int) and not isinstance(b, int):
            # Numeric identifiers sort before non-numeric ones
            return True
        if type(a) != type(b):
            return False
        if a < b:
            return True
        elif b < a:
            return False

    return len(lhs) < len(rhs)
