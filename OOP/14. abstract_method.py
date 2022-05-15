from abc import ABC, abstractmethod

class Father(ABC):
    
    @abstractmethod
    def func(self):
        print('Class Method')
        

obj = Father()

class Son(Father):
    
    pass