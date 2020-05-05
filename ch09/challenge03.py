import csv

my_list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movie_list.txt", "w") as f:
	w = csv.writer(f, delimiter=",")
	for name in my_list:
		w.writerow(name)

