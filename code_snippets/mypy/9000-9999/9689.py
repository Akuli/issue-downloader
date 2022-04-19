from typing import Callable

def mydeco(f: Callable) -> Callable:
    return f

# Failing case

def something():
    class Query:
        @mydeco
        def search(self, input: str) -> str:
            return input

    reveal_type(Query.search)

# Failing case

def something():
    @mydeco
    def example() -> str:
        return "str"
        
    reveal_type(example)

# Ok case

class Query:
    @mydeco
    def search(self, input: str) -> str:
        return input
        
reveal_type(Query.search)

# Ok case

@mydeco
def example() -> str:
    return "str"
    
reveal_type(example)
