# in operator used as a Membership Operator
# to find the Item in a Sequence


name = "Moin Abbas Malik"

find = "Malik"

check = find in name

if check:
    print(find, "Is Present in ", name)
else:
    print(find, "Not Present In", name)