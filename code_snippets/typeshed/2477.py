from six.moves import urllib
from typing_extensions import TYPE_CHECKING

if not TYPE_CHECKING:
    def reveal_type(ignored):
        pass

_, frg = urllib.parse.urldefrag("https://github.com/python/typeshed/#typeshed")
print(type(frg))
reveal_type(frg)

_, frg2 = urllib.parse.urldefrag(u"https://github.com/python/typeshed/#typeshed")
print(type(frg2))
reveal_type(frg2)

_, frg3 = urllib.parse.urldefrag(b"https://github.com/python/typeshed/#typeshed")
print(type(frg3))
reveal_type(frg3)
