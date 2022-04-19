from typing import Protocol

class A():
  def __init__(self, x: int) -> None:
    pass

class B(Protocol):
  def __call__(self) -> None:
    pass

def run(obj: B) -> None:
  obj()

def main() -> None:
  x = A
  run(x)

if __name__ == '__main__':
  main()
