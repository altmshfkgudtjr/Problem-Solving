# 완전탐색

def solution(brown, red):
	answer = []
	b_list = []
	for i in range(1, red + 1):
		if red % i == 0:
			b_list.append(i)
	for b in b_list:
		a = int((brown / 2) - b)
		if a*b - 2*b == red:
			answer = [a, b + 2]
			break
	return answer