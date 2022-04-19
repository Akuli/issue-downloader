def foo(node: Node) -> None:                                                     
    while node.next is not None:                                                 
        if node.value == node.next.value:                                        
            node.next = node.next.next                                           
        else:                                                                    
            node = node.next                                                     
