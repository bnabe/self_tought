
def f01(a):
	return(a // 2)

def f02(b):
	return(b * 4)

x = input("input number(int): ")
x = int(x)
"""
:param x: int.
"""

y = f01(x)
"""
:param y: int x//2.
"""

z = f02(y)
"""
:param z: int y*4.
"""

print(z)
