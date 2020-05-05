import csv

my_list = [["トップガン", "リスキービジネス", "マイノリティリポート"], ["タイタニック", "ザ・レベナント", "インセプション"], ["トレーニングデイ", "マン・オン・ファイア", "フライト"]]

with open("movie_list_j.txt", "w", encoding="utf-8") as f:
	w = csv.writer(f, delimiter=",")
	for name in my_list:
		w.writerow(name)

