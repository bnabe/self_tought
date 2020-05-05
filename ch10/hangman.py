import random

def hangman(word):
	wrong = 0
	stages = ["",
			"＿＿＿＿＿　　　　　",
			"｜　　　　｜　　　　",
			"｜　　　　｜　　　　",
			"｜　　　　＠　　　　",
			"｜　　　／｜＼　　　",
			"｜　　　／　＼　　　",
			"｜　　　　　　　　　"
			]
	rletters = list(word)
	board = ["_"] * len(word)
	win = False
	print("Welcome to HANGMAN!")

	while wrong < len(stages) -1:
		print("\n")
		char = input("Guess ONE character!:")

		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1

		print(" ".join(board))
		e = wrong + 1
		print("\n".join(stages[0:e]))

		if "_" not in board:
			print("You win!")
			print(" ".join(board))
			win = True
			break

	if not win:
		print("\n".join(stages[0:wrong+1]))
		print("You lost! The answer is {}.".format(word))

word_list = ["word", "list", "momo", "upon", "death"]
r_word = word_list[random.randint(0,len(word_list)-1)]
hangman(r_word)
