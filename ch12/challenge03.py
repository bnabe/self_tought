class Triangle:
	def __init__(self, under, tall):
		self.under = under
		self.tall = tall

	def area(self):
		return self.under * self.tall * 0.5

area01 = Triangle(20, 30)
print(area01.area())

