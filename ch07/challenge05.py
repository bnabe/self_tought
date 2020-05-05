list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
new_list = []

for i in list1:
	for j in list2:
		# print(i, j)
		new_list.append(i * j)

print(new_list)

