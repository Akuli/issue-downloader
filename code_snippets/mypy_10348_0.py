# error: "datetime" gets multiple values for keyword argument "tzinfo"
dt.datetime(*split_int_string(date, 4, 6, 8), *split_int_string(time, 2, 4))

# or

# error: "datetime" gets multiple values for keyword argument "tzinfo"
dt.datetime(*split_int_string(date, 4, 6, 8), *split_int_string(time, 2, 4), tzinfo=None)
