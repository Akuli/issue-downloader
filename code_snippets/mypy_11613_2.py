from datetime import timedelta
import arrow

a1 = arrow.get()
a2 = arrow.get()

diff: timedelta = a2 - a1
print(diff.total_seconds())
