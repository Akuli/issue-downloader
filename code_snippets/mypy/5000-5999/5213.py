class Item:
    def name(self) -> str: ...

def f(x: Item) -> None:
    print('name: {}'.format(x.name))  # No error, though should be x.name() 
    print('name: %s' % x.name)  # Similar to above
    foo(str(x.name))  # Ditto
