import cubed

while True:
	a = input("input number: ")
	try:
		a = int(a)
	except ValueError:
		continue
	
	y = cubed.cubed(a)
	print(y)

