class Add:
    
    def func(self, a, b):
        print("Addition : ", a + b)
    
class Multi(Add):
    
    def func(self, a, b):
        super().func(20, 2)
        print("Multiplication : ", a * b)

obj = Multi() 
obj.func(10, 6)