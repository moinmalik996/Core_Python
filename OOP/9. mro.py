class Father:
    
    def __init__(self):
        super().__init__()
        print('Father Constructor is called')
    

class Mother:
    
    def __init__(self):
        super().__init__()
        print('Mother Constructor is called')
        
        
class Son(Father, Mother):
    
    def __init__(self):
        super().__init__()
        print('Son Constructor is called')
        
obj = Son()