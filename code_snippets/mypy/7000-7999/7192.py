assert isinstance(email, EmailMessage)

# Fine
r1 = email.get("List-Id", "")
# Fine
r2 = email.get("List-Id", "") or email.get("List-Unsubscribe", "")
# Fine
r3 = bool(email.get("List-Id", "") or email.get("List-Unsubscribe", ""))
# FAILS: Argument 2 to "get" of "Message" has incompatible type "str"; expected "bool"
r4 = bool(
    email.get("Auto-Submitted", "") in ("no", "")
    or email.get("List-Unsubscribe", "")
)
# FAILS: Argument 2 to "get" of "Message" has incompatible type "str"; expected "bool"
r5 = email.get("Auto-Submitted", "") in ("no", "") or email.get(
    "List-Unsubscribe", ""
)

_T = TypeVar('_T')

class Message:
    ...
    def get(self, name: str, failobj: _T = ...) -> Union[_HeaderType, _T]: ...
