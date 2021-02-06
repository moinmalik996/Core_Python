import random
import secrets

a = random.randrange(1, 10)
b = random.normalvariate(0, 1)

print(a)
print(b)

mylist = list("ABCDEFG")
a = random.choice(mylist)
b = random.choices(mylist, k=3)  # k is the no. of elements to choose

print(a)
print(b)

random.shuffle(mylist)
print(mylist)

a = secrets.randbelow(10)
print(a)