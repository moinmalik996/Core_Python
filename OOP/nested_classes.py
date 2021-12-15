class Soldier:
    def __init__(self):
        self.name = "Moin"
        self.gn   = self.Gun()

    def show_data(self):
        print("Name is : ", self.name)

    class Gun:
        def __init__(self):
            self.name = "AK47"
            self.capacity = "47 Rounds"
            self.price = "50k PKR"

        def show_data_inner(self):
            print("Gun Name : ", self.name)
            print("Gun Capacity : ", self.capacity)
            print("Gun Price : ", self.price)


myobj = Soldier()

print(myobj.name)
myobj.show_data()

print()
print("Print Inner Class Data\n")

g = myobj.gn
g.show_data_inner()

