n = int(input())
lst = list(map(int, input().split()))
lst.reverse()
for i, elem in enumerate(lst): #enumerateを使うことで、リストのインデントと要素を取り出せる
	if 0 < i:
		print(" ", end = "") #最初以外の要素の前にスペースをつける。
	print(elem, end = "")    #最後は要素がなくなるから、　end = "" の形にする
print()	#改行
