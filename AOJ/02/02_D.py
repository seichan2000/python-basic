W, H, x, y, r = map(int, input().split())
if x >= r and y >= r:
	if x + r <= W and y + r <= H:
		print("Yes")
	else:
		print("No")
else:
	print("No")
