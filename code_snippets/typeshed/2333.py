import urllib.request
from typing import Optional

resp = urllib.request.urlopen('https://example.com')
x: Optional[str] = resp.headers['connection']
