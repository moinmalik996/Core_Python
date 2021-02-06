 # Erros and Exceptions

try:
    a = 5 / 1
    b = a + 1
except ZeroDivisionError as zd:
        print(zd)
except TypeError as te:
    print(te)
else:
    print('Everything is fine.') 
finally:
    print("Okay")
    
   
   
     
class valueError(Exception):
    pass


def testvalue(x):
    if x > 100:
        raise valueError("Value is too high")
    
try:
    testvalue(200)
except valueError as e:
    print(e)