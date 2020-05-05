
musician = {
		"Babymetal": [
			"Pa Pa Ya!",
			"Shanti Shanti Shanti",
			"Da Da Dance",
		],
		"passcode": [
			"MISS UNLIMITED",
			"Ray",
			"ONE STEP BEYOND",
		],
		"King GNU": [
			"白日",
			"傘",
			"飛行艇",
		],
}
#print(type(musician))
m_name = input("ミュージシャンの名前を入力してください。: ")
if m_name in musician:
	print(musician[m_name])
else:
	print("見つかりません。")

