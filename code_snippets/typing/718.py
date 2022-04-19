# foo accepts a date object, but allows to add and access
# unknown attributes at runtime. It basically treats date
# as having __getattr__()/__setattr__() methods.
def foo(date: Dynamic[datetime.date]) -> None:
    date.my_attr = 123
    print(date.added_by_called)


# typing.dynamic() is a no-op at runtime and basically an alias
# for cast(Generic[X], y) at type-check time, where X is the
# type of y.
# In this example, dt has type Dynamic[datetime.date].
dt = dynamic(datetime.date.today())
foo(dt)

# The following would also work:
foo(datetime.date.today())
other_dt: datetime.date = dt

class Monkey(Protocol):
    donkey: int

def foo(dt: Dynamic[datetime.date, Monkey]) -> None:
    # ok:
    print(dt.year)
    dt.donkey += 3
    # errors:
    print(dt.kong)
    dt.donkey += ""

dt = dynamic(datetime.date.today(), Monkey)
