class Mobile:
    _finger_print = "Yes"               # class variable

    def __init__(self):                 
        self.model = "RealMe X"         # instance variable

    def show_model(self):               # instance method
        print("Model : ", self.model)   # accessing instance variables

    @classmethod
    def my_method(cls):
        is_fp = cls._finger_print       # accessing class variable
        print(is_fp)


realme = Mobile()
realme.show_model()
Mobile.my_method()

print()

Mobile._finger_print = "No"

realme = Mobile()
realme.show_model()
Mobile.my_method()