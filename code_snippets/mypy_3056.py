class C(object):
  def __del__(self, a):
    # type: (int) -> int
    return a

class C(object):
  def __del__(self):
    # type: () -> int
    return 0

