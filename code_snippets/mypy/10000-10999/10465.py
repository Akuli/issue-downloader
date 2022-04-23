items = (foo.bar for foo in all_the_foos)
for x in y:
    if x in items:
        do_sparkle_hands_stuff()

y in (x.foo for x in foos)

any(y == x.foo for x in foos)

for y in sorted_y:
    if y in sorted_x:  # sorted_x is an iterator
        ...
