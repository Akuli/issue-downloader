@counter
def greet(name: str) -> str:
    return f'hello, {name}'

print(greet('John'))
print(f'greet() called {greet.count} times')
