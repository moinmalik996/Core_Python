class Dog:
    
    def walk(self):
        print("Dog is Walking")

class Cat:
    
    def walk(self):
        print('Cat is walking')
        
def func(obj):
    obj.walk()
    
s = Dog()

func(s)