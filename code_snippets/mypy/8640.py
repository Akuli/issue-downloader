gen = (3 * x for x in range(10))  # revealed type: Generator[int, None, None]
for i in gen:
    print(i)

for i in gen:
    print(i)
