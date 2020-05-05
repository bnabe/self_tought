import math

class Circle:
	def __init__(self, r):
		self.radius = r

	def area(self):
		return self.radius * self.radius * math.pi

a1 = Circle(20)
print(a1.area())
