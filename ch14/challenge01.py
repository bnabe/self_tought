class Rectangle:
	def __init__(self, width, hight):
		self.width = width
		self.hight = hight

	def calculate_perimeter(self):
		return (self.width + self.hight) * 2

class Square:
	square_list = []

	def __init__(self, width):
		self.width = width
		self.square_list.append(width)

	def calculate_perimeter(self):
		return self.width * 4
	
	def change_size(self, c_width):
		self.width -= c_width

	def print_square(self):
		print("{} by {} by {} by {} ".format(self.width, self.width, self.width, self.width))

a1 = Rectangle(20, 30)
print(a1.calculate_perimeter())

c1 = Square(20)
print(c1.calculate_perimeter())
c1.change_size(10)
print(c1.calculate_perimeter())

print(Square.square_list)
c1.print_square()
