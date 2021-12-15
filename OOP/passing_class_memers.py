class Student:

    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    # Instance Method
    def show_data(self):
        print("Name : ", self.name)
        print("Age  : ", self.age)


class User:

    @staticmethod
    def show(cls):
        print("Passing to Name : ", cls.name)    # Passing Instance Variables
        print("Passing to Age  :", cls.age)      # Same
        cls.show_data()                          # Passing Instance Method


myObject = Student("Moin", "25")

User.show(myObject)
