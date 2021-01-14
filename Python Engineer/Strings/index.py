#Strings  : Ordered , Immutable , text representation

# mystring = "Hello World"
# substring = mystring[ : 5]

# print(mystring)
# print(substring)

name = 'Moin Malik'
greetings = "Hi ! "

string = greetings + " " + name
print(string)

print(name)
print(name.strip())                         # Removes White Spaces
print(name.upper())                         # Convert Into Upper Case
print(name.startswith('H'))                 # Return True or False
print(name.find('o'))                       # Gives the index of String : If not found it gives -1
print(name.count('i'))                      # Count no. of a character in a string
print(name.replace('Malik', 'Abbas'))       # Replace Characters with some other Characters
new_name = name.split(' ')                  # Split strings in a list
print(new_name)
name = ' '.join(new_name)
print(name)


# FORMATTING STRINGS 
# %  ,  format  ,  f-strings

var = "Moin"
var1 = 34
var2 = 12.5678

print("The Variable is %s" %var)
print("The Variable is %d" %var1)
print("The Variable is %.2f" %var2)
# sing .format method
print("The Variables using format method are {}, {} and {:.2f}".format(var, var1, var2))
#using f-strings method
var1 = 23.67
var2 = 56

print(f"The new variables are {var1} , {var2}")

