def gcd(x, y):
	while y:
		x, y = y, x % y
	return x

def solution(w, h):
	value = gcd(w, h)
	pattern = (w / value) + (h / value) - 1
	return int(w  * h - pattern * value)