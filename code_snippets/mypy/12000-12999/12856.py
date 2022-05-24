from wsgiref.types import WSGIEnvironment, StartResponse, InputStream
from typing import Iterable

def f(a: str) -> int:
	return int(a)

def wsgi_callable(environ: WSGIEnvironment, start_response: StartResponse) -> Iterable[bytes]:
	# No error:
	content_length1 = f(environ['CONTENT_LENGTH'])

	# error: Expression has type "Any":
	content_length2 = f("0" if environ['CONTENT_LENGTH'] == "" else environ['CONTENT_LENGTH'])

	return []
