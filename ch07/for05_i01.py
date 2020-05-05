tv = ["GOT", "Narcos", "Vice"]
print(tv)

i = 0
for show in tv:
	new = tv[i]
	new = new.upper()
	tv[i] = new
	i += 1

print(tv)

