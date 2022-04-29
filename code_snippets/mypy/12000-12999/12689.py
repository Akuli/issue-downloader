# pkg/lib.py

# implicit re-exports
import requests
import requests as demands
import requests.status_codes as requests_status_codes
from requests import Request

# implicit submodule re-export, but mypy doesn't care
from requests import status_codes

# pkg/shell.py

from pkg.lib import requests, demands, requests_status_codes, Request, status_codes
