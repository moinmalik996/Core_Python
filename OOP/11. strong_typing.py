class Dog:
    
    def walk(self):
        print("Dog is Walking")

class Cat:
    
    def walk(self):
        print('Cat is walking')
        
class Snake:
    
    def run(self):
        print('Snake is running')
        

def func(obj):
    if hasattr(obj, "walk"):
        obj.walk()
    if hasattr(obj, 'run'):
        obj.run()
    else:
        print('Error : Method is not defined')
    
s = Snake()

func(s)