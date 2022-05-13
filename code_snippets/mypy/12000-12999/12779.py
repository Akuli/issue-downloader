from flask import current_app
from werkzeug.exceptions import abort as _wz_abort

# current_app is annotated as `current_app: Flask`
# Flask.aborter is an instance of werkzeug.exceptions.Aborter
# Aborter.__call__ is annotated as `--> NoReturn`

def abort(code: int, *args: Any, **kwargs: Any) -> NoReturn:
    reveal_type(current_app)
    reveal_type(current_app.aborter)
    reveal_type(current_app.aborter.__call__)
    reveal_type(_wz_abort)

    # Both of the following calls are annotated
    # with NoReturn, and reveal_type shows that.

    if current_app:
        current_app.aborter(code, *args, **kwargs)

    _wz_abort(code, *args, **kwargs)
