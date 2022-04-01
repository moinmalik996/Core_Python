
class MyClass():
    
    title = 'My Standard'
    
    def __init__(self):
        self.age = '28'
        
    def show_age(self):
        print("Age is    :   ", self.age)
        
    @classmethod
    def cls_method(cls):
        print("Class Title  :   ", cls.title)
        

sam = MyClass()

sam.show_age()
sam.cls_method()
MyClass.cls_method()