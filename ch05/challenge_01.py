
musician = ["Babymetal", "passcode", "KingGNU", "Band-maid", "Man with a mission"]

tokyo = (139.45,35.41)
atsugi = (139.42,35.45)
iwakuni = (34.17,132.22)

masa = {"tall": "182",
		"weights": "75",
		"eyes": "brown",
		"hair": "black",
}

search = input("キーを入力してください。:")
if search in masa:
	print(masa[search])
else:
	print("入力されたキーは見つかりません。")

