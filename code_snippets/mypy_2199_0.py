from typing import *
a = ['x', None]  # type: List[Optional[str]]
for i in range(len(a)):
    if a[i]:
        print(i, '<' + a[i] + '>')
