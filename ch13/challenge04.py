class Horse:
	def __init__(self, name, hight, length, weight):
		self.name = name
		self.hight = hight
		self.length = length
		self.weight = weight

class Rider:
	def __init__(self, name, age, horse):
		self.name = name
		self.age = age
		self.horse = horse

gred_the_horse = Horse("Gred", 180, 150, 300)
mike = Rider("J. Michel", 30, gred_the_horse)
print(mike.horse.name, mike.horse.weight)
