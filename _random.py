import random

value = random.random()  # generate number between 1 and 0
value1 = random.uniform(1, 10)
value2 = random.randint(1, 10)


print(value)
print(value1)
print(value2)
print()

greetings = ['Moin', 'Malik', 'Junaid']

str1 = random.choice(greetings)
str2 = random.choices(greetings, weights=[5, 5, 2], k=10)

print('Hey', str1)
print(str2)
print()

deck = list(range(1, 50))
random.shuffle(deck)
print(deck)


