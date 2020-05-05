class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

nino = Person("Nino San", 20)
a_nino = nino
print(nino is a_nino)
ninosan = Person("Nino San", 20)
print(nino is ninosan)
