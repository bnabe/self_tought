class Rectangle:
	def __init__(self, width, hight):
		self.width = width
		self.hight = hight

	def calculate_perimeter(self):
		return (self.width + self.hight) * 2

class Square:
	def __init__(self, width):
		self.width = width
	
	def calculate_perimeter(self):
		return self.width * 4
	
	def change_size(self, c_width):
		self.width -= c_width

a1 = Rectangle(20, 30)
print(a1.calculate_perimeter())

c1 = Square(20)
print(c1.calculate_perimeter())
c1.change_size(10)
print(c1.calculate_perimeter())

