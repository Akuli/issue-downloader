import io
import sys

class C(io.BufferedIOBase):
  pass

def test(c: io.BufferedIOBase):
  assert isinstance(c, io.BufferedIOBase)

test(sys.stdout.buffer)
test(C())
