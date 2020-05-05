my_list = []

with open("henshin.txt", "r", encoding="shift-jis") as f:
	my_list.append(f.read())

print(my_list)

