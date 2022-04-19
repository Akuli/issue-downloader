from typing import Any
from typing import AnyStr
from typing import Generic


class Message(Generic[AnyStr]):
    header: AnyStr
    content: AnyStr

    def __init__(self, header: AnyStr, content: AnyStr) -> None:
        self.header = header
        self.content = content

# This feels wrong to me, and I'd rather see this as Union[Message[str], Message[bytes]]
m1: Message = Message(header="foo", content="bar")
reveal_type(m1)  # Message[Any]...

# This is perhaps ok, since the user explicitly passed the `Any` parameter. But if this behavior is kept, 
# one shouldn't be forced to provide a type arg to restricted generics in strict mode, since that 
# would imply having to enumerate the restriction to get the same behavior as above.
m2: Message[Any] = Message(header="foo", content="bar")
reveal_type(m2)  # Message[Any]...
