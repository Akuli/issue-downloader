#!/usr/bin/env python
from typing import Any, Callable, Optional, TypeVar
import socket, sys

class CodedException(Exception):
    code = None # type: int
class CommandLineError(CodedException): code = 3

T = TypeVar('T')

def of_string_werr(fc # type: Callable[..., T]
):
    # type: (...) -> Callable[[Callable[[], Any]], Callable[[str], Callable[..., T]]]
    def curry_handler(fh):
        # type: (Callable[[], Any]) -> Callable[[str], Callable[..., T]]
        def curry_arg(x): # type: (str) -> Callable[..., T]
            def mkf(*args, **kw):
                # type: (*Any, **Any) -> T
                try: return fc(x, *args, **kw)
                except ValueError: fh()
            return mkf
        return curry_arg
    return curry_handler

def int_of_string_werr(fh):
    # type: (Callable[[], Any]) -> Callable[[str], Callable[..., int]]
    return of_string_werr(int)(fh)

def fail(ex=None): # type: (Optional[CodedException]) -> None
    if ex:
        print('%s: error: %s' % (sys.argv[0], ex), file=sys.stderr)
        sys.exit(ex.code)
    else:
        print('doop', file=sys.stderr)
        sys.exit(CommandLineError.code)

def ff(): # type: () -> None
    fail(CommandLineError('port must be an integer'))

# XXX the buggy line; should be: port = int_of_string_werr(ff)('1234')()
port = int_of_string_werr(ff)('1234')
# reveal_type(port): def (*Any, **Any) -> builtins.int

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# XXX typechecks but fails at runtime with
# TypeError: an integer is required (got type function)
sock.connect(('blah', port))

#!/usr/bin/env python
from typing import Any, Callable, Optional, TypeVar
from functools import partial
import socket, sys

class CodedException(Exception):
    code = None # type: int
class CommandLineError(CodedException): code = 3

T = TypeVar('T')

def of_string_werr(fc # type: Callable[..., T]
):
    # type: (...) -> Callable[[Callable[[], Any]], Callable[[str], partial[T]]]
    def curry_handler(fh):
        # type: (Callable[[], Any]) -> Callable[[str], partial[T]]
        def curry_arg(x): # type: (str) -> partial[T]
            def mkf(*args, **kw):
                # type: (*Any, **Any) -> T
                try: return fc(x, *args, **kw)
                except ValueError: fh()
            return partial(mkf)
        return curry_arg
    return curry_handler

def int_of_string_werr(fh):
    # type: (Callable[[], Any]) -> Callable[[str], partial[int]]

    # XXX
    # Incompatible return value type (got Callable[[str], partial[object]],
    # expected Callable[[str], partial[int]])
    return of_string_werr(int)(fh)

def fail(ex=None): # type: (Optional[CodedException]) -> None
    if ex:
        print('%s: error: %s' % (sys.argv[0], ex), file=sys.stderr)
        sys.exit(ex.code)
    else:
        print('doop', file=sys.stderr)
        sys.exit(CommandLineError.code)

def ff(): # type: () -> None
    fail(CommandLineError('port must be an integer'))

# XXX the buggy line; should be: port = int_of_string_werr(ff)('999')()
port = int_of_string_werr(ff)('999')
# reveal_type(port): def (*Any, **Any) -> builtins.int

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# XXX typechecks but fails at runtime with
# TypeError: an integer is required (got type function)
sock.connect(('blah', port))

