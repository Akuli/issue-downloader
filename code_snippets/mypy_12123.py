from typing import Optional

class Test:    
    def double(self, x: int) -> int:
        return x * 2

def check_value(a: Optional[Test], b: Optional[int]) -> Optional[int]:
    if None in (a, b):
        return None
    
    return a.double(b)
    
if __name__ == '__main__':
    check_value(Test(), 2)
