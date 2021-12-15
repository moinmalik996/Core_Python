class Myclass:
	def show(self):
		print("I am a method")


class Mobile:
	def __init__(self):
		self.model = "RealMe X"
	
	def show_model(self):
		price = 30000
		print("Model:", self.model, "\nPrice:", price)


a = Myclass()
a.show()

b = Mobile()
b.show_model()
print()
print(b.model)

