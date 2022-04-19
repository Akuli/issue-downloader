import sys
from types import TracebackType
from typing import Optional as Opt, Tuple, Type, Union

class Event:
	exc_info: Opt[Union[Tuple[Type[BaseException],BaseException,TracebackType],Tuple[None,None,None]]] = None

def foo ( event: Event ) -> None:
	try:
		assert False
	except Exception:
		event.exc_info = *sys.exc_info() # mypy crashes on this syntax error
	
event = Event()
foo ( event )
print ( repr ( event.exc_info ) )
