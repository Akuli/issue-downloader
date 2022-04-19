if foo():
    x = 0
    print(x)
else:
    x = 'a'  # Define a new variable?
    print(x)

for x in [1, 2]:
    print(x)
if foo():
    for x in ['a', 'b']:  # Define a new variable?
        print(x)

