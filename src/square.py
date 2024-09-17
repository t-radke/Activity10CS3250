class Square: 

    # faulty constructor on purpose
    def __init__(self, side) -> None:
        pass

    def area(self): 
        return self.side * self.side 
    
    # faulty method on purpose
    def perimeter(self): 
        return self.side * 2
