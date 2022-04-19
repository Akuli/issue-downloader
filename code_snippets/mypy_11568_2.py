if sys.version_info >= (3, 8):
    from typing import Final, Literal, _TypedDictMeta  # type: ignore[attr-defined] # noqa: F401
else:
    from typing_extensions import (  # type: ignore[attr-defined] # noqa: F401
        Final, Literal, _TypedDictMeta,
    )
