class A:
    @counter
    def greet(self, name: str) -> str:
        return f'hello, {name}'

a = A()
print(a.greet('John'))  # error
print(f'greet() called {a.greet.count} times')
