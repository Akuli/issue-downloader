class A:

    def __init__(self, return_tuple=False):
        self.return_tuple = return_tuple
    
    def __call__(self):
        if self.return_tuple:
            return (1, 2)
        return 1

