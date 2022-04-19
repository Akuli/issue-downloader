from typing import Optional 
 
 
class Foo: 
    bar: Optional[int] 
 
    def thing(self) -> int: 
        if self.bar is None: 
            return 0 
        self.set_bar_to_none() 
        return self.bar 
 
    def set_bar_to_none(self) -> None: 
        self.bar = None 
