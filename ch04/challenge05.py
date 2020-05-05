
def f():
	try:
		x = input("input number: ")
		"""
		:param x: str.
		"""
		x = float(x)
		"""
		:param x: float.
		"""
		print(x)
	except ValueError:
		print("Invalid input.")

f()

