from typing import List

class Upi(object):
    pass


class Subi(Upi):
    pass


subs = [Subi(), Subi()]
ok1:List[Upi] = [s for s in subs]
ok2:List[Upi] = list(subs)
notOk:List[Upi] = subs[:] # this should also be ok IMHO
