str1 = "Moin"

str2 = " Malik"

print("String Formatting Using .format()")
print("{0}  {1}".format(str1, str2))
print("{1}  {0}".format(str1, str2))

print("Formatting Using f-style Format")

str3 = str1 + str2

print(f"{str3}")
print(f"{str3:15s}")
print(f"{str3:<15}")
print(f"{str3:*<15}")
print(f"{str3:*>15}")
print(f"{str3:>15}")
print(f"{str3:^16}")


