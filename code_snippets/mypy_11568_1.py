from drf_spectacular.drainage import (
    Final, Literal, error, get_view_method_names, isolate_view_method, set_override, warn,
)
...
Direction = Literal['request', 'response']
