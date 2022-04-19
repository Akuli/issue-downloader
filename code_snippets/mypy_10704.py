import functools

@functools.cache
def factorial(n: int) -> int:
    return n * factorial(n-1) if n else 1    

def identity(n: int) -> int:        
    return n

if __name__ == '__main__':
    print(factorial.__name__, factorial.__annotations__)
    print(identity.__name__, identity.__annotations__)
    factorial("")
    identity("")
