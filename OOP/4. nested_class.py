class Army():
    
    def __init__(self):
        self.name = 'Malik'
        self.gn   = self.Gun()
        
    def show(self):
        print(f"Name is : {self.name}")
        
    class Gun():
        
        def __init__(self):
            self.name     = "AK 47"
            self.capacity = '65 Rounds'
            self.range    = '50m'
            
        def disp(self):
            print(f'Name     : {self.name}')
            print(f'Capacity : {self.capacity}')
            print(f'Range    : {self.range}')
            

a = Army()
a.show()
print(type(a))