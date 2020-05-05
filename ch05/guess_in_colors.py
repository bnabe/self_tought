colors = ["purple", "orange", "green"]

guess = input("何色でしょう？（入力してください。）: ")
""":param guess: str.
"""

if guess in colors:
	print("あたり！")
else:
	print("ハズレ！また挑戦してね。")

