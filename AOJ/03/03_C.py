while 1:
	x, y = map(int, input().split())
	if x == 0 and y == 0:
		break
	else:
		print("%d %d" % (min(x, y), max(x, y)))
