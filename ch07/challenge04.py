ans = [5, 10]

while True:
	n = input("数字を入力するか、qで終了します。:")

	if n == "q":
		break
	
	try:
		n = int(n)
	except ValueError:
		continue

	if n in ans:
		print("正解です！")
	else:
		print("不正解です！")


