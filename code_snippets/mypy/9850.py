foo: List[Literal['a', 'b']] = ['a', 'b', 'a']

if foo[0] == 'a':
    print('a')
    exit()

foo.pop(0)
reveal_type(foo[0])
if foo[0] == 'a':
    pass
