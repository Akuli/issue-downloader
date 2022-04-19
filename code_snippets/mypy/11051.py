from typing import Optional

class Global:
  attr: Optional[int] = None

G = Global()

def f() -> None:
  G.attr = 1

def t() -> None:
  G.attr = None
  f()
  assert G.attr is not None
  reveal_type(G)
