# t.py
import sys

if sys.version_info < (3, 0):
    unicode = unicode
    chr = unichr
else:
    unicode = str
