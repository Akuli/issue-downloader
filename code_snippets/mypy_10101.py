from typing import Any

typ_a = Any
typ_b = Any
def test1(x: typ_a, y: typ_b): pass

from typing import Any

typ_a, typ_b = Any, Any
def test2(x: typ_a, y: typ_b): pass

typ_a = typ_b = Any
def test3(x: typ_a, y: typ_b): pass

