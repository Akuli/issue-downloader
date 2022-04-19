# bad.py

from sys import platform
assert platform == "win32"

from ctypes import WINFUNCTYPE, windll, WinError, get_last_error
