from typing import *
a = ['x', None]  # type: List[Optional[str]]
for i in range(len(a)):
    if a[i]:
        print(i, '<' + a[i] + '>')

for i in range(len(a)):
    ai = a[i]
    if ai:
        print(i, '<' + ai + '>')
