import typing

x = 'Hagar Qim'

def f() -> None:
  global x, y
  x = 1  # Type error reported
  y = 2  # Ignored

y = 'Mnajdra'
