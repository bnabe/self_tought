
try:
	a = input("type a number:")
	b = input("type another:")
	a = int(a)
	b = int(b)
	"""
	:param a: int first number.
	:param b: int second number.
	:print: float a/b
	"""
	print(a / b)
except(ZeroDivisionError, ValueError):
	print("Invalid input.")

