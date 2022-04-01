class Mobile():
    
    name = 'Moin'

    def __init__(self):
        self.model = "Samsung"

    def show_data(self, p):
        price = p
        print("Model : ", self.model)
        print("Price : ", price)


sam = Mobile()
sam.show_data(800)

name = print(sam.name)
