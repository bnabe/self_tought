class Shape:
	def __init__(self):
		pass

	def what_am_i():
		return "I am a shape."

class Rectangle(Shape):
	pass

class Square(Shape):
	pass

print(Rectangle.what_am_i())
print(Square.what_am_i())
