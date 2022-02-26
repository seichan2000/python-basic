import math

def are(r):
	S = math.pi * (r**2)
	return(S)

def length(r):
	L = math.pi * 2 * r
	return(L)

r = float(input())
print("%f %f" % (are(r), length(r)))
