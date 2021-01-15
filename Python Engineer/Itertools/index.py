# IterTools : Product, Permutations, Combinations, Accumulate, Groupby and Infinite Iterations
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat

# PRODUCUCT
a = [1, 2]
b = [3]
print("PRODUCTS  :  \n")
prod = product(a, b)
print(list(prod))
prod = product(a, b, repeat=2)
print(list(prod))


# PERMUTATIONS
a = [1, 2, 3]
print("\nPERMUTATIONS  :  \n")
permu = permutations(a)
print(list(permu))
permu = permutations(a, 2)  # 2 is length of the permutation.
print(list(permu))

# COMBINATIONS
a = [1, 2, 3, 4]
print("\nCOMBINATIONS  :  \n")
comb = combinations(a, 2) # 2 in the length of a Combination
print(list(comb))
comb = combinations_with_replacement(a, 2)
print(list(comb))

# ACCUMULATE 
print("\nACCUMULATE  :  \n")
a = [1, 2, 5, 3, 4]
accu = accumulate(a)
print(a)
print(list(accu))
accu = accumulate(a, func=max) # It cannot exceed the sum more than 4
print(a)
print(list(accu))

#GROUPBY
print("\nGROUP-BY  :  \n")

a = [1, 2, 3, 4]
# def smaller_than_3(x):
#     return x < 3
group_obj = groupby(a, key=lambda x: x < 3)  # Group the elements in item grater than 3 as True
for(key, value) in group_obj:
    print(key, list(value))
    
    
persons = [{'name': 'Moin Malik', 'Age': 12},{'name': 'Hamza', 'Age': 12},
     {'name': 'Junaid', 'Age': 34},{'name': 'Saad', 'Age': 13}]

per_groupby = groupby(persons, key=lambda x: x['Age'])  # Group Elements by Their Age and Make a List
for(key, item) in per_groupby:
    print(key, list(item))
    
    
# COUNT , CYCLE, REPEAT 

for i in count(1):
    print(i)
    if i == 15:
        break
    
a = [2, 3, 4]

for i in cycle(a):
    print(i)