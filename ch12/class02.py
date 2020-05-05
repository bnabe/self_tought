class Orange:
	def __init__(self, w, c):
		self.weight = w
		self.color = c
		self.mold = 0
		print("Created!")

	def rot(self, days, temp):
		self.mold = days * temp

orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)

