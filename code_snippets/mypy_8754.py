#!/usr/bin/env python3

from typing import (
	Any,
	Callable,
)

import requests
import tenacity

# Keep trying the request until we connect.
@tenacity.retry(retry=tenacity.retry_if_exception_type(requests.exceptions.ConnectionError))
def retry_if_connection_error(func: Callable[..., requests.Response], *args: Any, **kwargs: Any) -> requests.Response:
	return func(*args, **kwargs)

# Keep trying the request unless we connect.
@tenacity.retry(retry=tenacity.retry_unless_exception_type(requests.exceptions.ConnectionError))
def retry_unless_connection_error(func: Callable[..., requests.Response], *args: Any, **kwargs: Any) -> requests.Response:
	return func(*args, **kwargs)
