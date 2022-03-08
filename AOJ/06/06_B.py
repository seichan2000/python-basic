l = [[0 for i in range(13)] for j in range(4)] #2次元配列の初期化
n = int(input())
for i in range(n):
	mark, num = input().split()
	num = int(num)
	if mark == "S":
		l[0][num - 1] = num
	elif mark == "H":
		l[1][num - 1] = num
	elif mark == "C":
		l[2][num - 1] = num
	elif mark == "D":
		l[3][num - 1] = num
for i in range(4):
	for j in range(13):
		if i == 0 and l[i][j] == 0:
			print("S %d" % (j + 1))
		elif i == 1 and l[i][j] == 0:
			print("H %d" % (j + 1))
		elif i == 2 and l[i][j] == 0:
			print("C %d" % (j + 1))
		elif i == 3 and l[i][j] == 0:
			print("D %d" % (j + 1))
