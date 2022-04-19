_T = TypeVar("_T", str, bytes)

class Formatter(Generic[_T]):
    @overload
    def __init__(self: Formatter[str], *, encoding: None = ..., outencoding: None = ..., **options) -> None: ...
    @overload
    def __init__(self: Formatter[bytes], *, encoding: str, outencoding: None = ..., **options) -> None: ...
    @overload
    def __init__(self: Formatter[bytes], *, encoding: None = ..., outencoding: str, **options) -> None: ...

from pygments.formatters.html import HtmlFormatter

reveal_type(HtmlFormatter())
reveal_type(HtmlFormatter(encoding='utf-8'))
