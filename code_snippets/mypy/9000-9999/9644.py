class TestObject(object):
   __slots__ = ["a", "b"]
   a: int
   b: str

   def __init__(self, a: int, b: str) -> None:
      self.a = a
      self.b = b

def test() -> None:
   x = TestObject(5, "hi")
   reveal_type(TestObject.a)
   reveal_type(TestObject.b)
   reveal_type(x.a)
   reveal_type(x.b)
