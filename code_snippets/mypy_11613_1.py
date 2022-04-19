import arrow

a1 = arrow.get()
a2 = arrow.get()

diff = a2 - a1
print(diff.total_seconds())
