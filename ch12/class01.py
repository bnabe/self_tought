class Orange:
	def __init__(self, w, c):
		self.weight = w
		self.color = c
		print("Created!")

or1 = Orange(10, "dark orange")
print(or1.weight)
print(or1.color)

or1.weight = 100
or1.color = "light orange"
print(or1.weight)
print(or1.color)

or2 = Orange(4, "light orange")
or3 = Orange(8, "dark orange")
or4 = Orange(14, "yellow")

