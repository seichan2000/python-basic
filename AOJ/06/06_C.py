home = [[[0 for i in range(10)] for j in range(3)] for k in range(4)] #3次元配列の初期化
n = int(input())
for i in range(n):
	b, f, r, v = map(int, input().split())
	home[b - 1][f - 1][r - 1] += v
for i in range(4):
	for j in range(3):
		for k in range(10):
			print(" %d" % (home[i][j][k]), end = "")
		print()
	if i < 3: #1~3棟の後に＃を20個つける
		print("####################", end = "")
		print()
