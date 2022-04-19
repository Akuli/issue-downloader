#! /usr/bin/env python

import re

m = re.match(u"(?P<key1>[01]+)", u"100 abc")
    
if m is not None:
    d = m.groupdict()
    print(type(list(d.items())[0][0]))
    print(d.get(u"key1", u"default"))
