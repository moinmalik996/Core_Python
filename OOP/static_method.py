# Static methods cannot access Class Variables. They are just ordinary 
# methods to get arguments and return some data. Utility purpose.
# They do not contain any default cls argument

class Mobile:

    @staticmethod
    def show_data(name, price):
        n = name
        p = price
        print("Name : ", n, "\nPrice : ", p)

mobile = Mobile()
Mobile.show_data("Samsung", "10 Lakh")