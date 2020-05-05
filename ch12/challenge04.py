class Hexagon:
	def __init__(self, length):
		self.length = length

	def calcurate_total_length(self):
		return self.length * 6

length01 = Hexagon(40)
print(length01.calcurate_total_length())

