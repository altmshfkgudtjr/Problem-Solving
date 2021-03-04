def ten2three(n):
	base = "0123456789"
	s, r = divmod(n, 3)
	if s == 0:
		return base[r]
	else:
		return ten2three(s) + base[r]

def three2ten(n):
	output = 0
	n = str(n)[::-1]
	for i, v in enumerate(n):
		output += (3 ** i) * int(v)
	return output

def solution(n):
	answer = ten2three(n)
	answer = int(str(answer)[::-1])
	return three2ten(answer)