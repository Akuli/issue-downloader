from typing import Optional                                                      
                                                                                 
                                                                                 
class Node:                                                                      
    def __init__(self, value: int):                                      
        self.value = value                                                       
        self.next: Optional[Node] = None                                         
                                                                                 
                                                                                 
def foo(node: Node) -> None:                                                     
    while node.next is not None:                                                 
        if node.value != node.next.value:                                        
            node = node.next                                                     
        else:                                                                    
            node.next = node.next.next   # <-- HERE

def foo(node: Node) -> None:                                                     
    while node.next is not None:                                                 
        if node.value == node.next.value:                                        
            node.next = node.next.next                                           
        else:                                                                    
            node = node.next                                                     

