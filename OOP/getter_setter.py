# class Mobile:

#     def __init__(self):
#         self.model = "Realme X"

#     def get_model(self):                  to get the data wo simple use get_ function
#         return self.model

# realme = Mobile()
# print(realme.get_model())


class Mobile:

    def __init__(self):
        self.model = "Realme 1"

    def set_model(self, name):
        self.model = name

realme = Mobile()

realme.set_model("RealMe 2")
print(realme.model)


