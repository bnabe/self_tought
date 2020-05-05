
songs = {"1": "fun",
		 "2": "blue",
		 "3": "me",
		 "4": "floor",
		 "5": "live"
		}

n = input("数字を入力して下さい。(1-5): ")
if n in songs:
	song = songs[n]
	print(song)
else:
	print("見つかりません。")

