cnt = 0
a, b, c = map(int, input().split())
for i in range(a, b + 1):
	if c % i == 0:
		cnt += 1
	i += 1
print("%d" % (cnt))
