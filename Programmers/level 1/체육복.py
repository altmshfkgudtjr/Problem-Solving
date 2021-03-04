# 그리디

def solution(n, lost, reserve):
	answer = 0
	suits = [1] * n
	for i in lost:
		suits[i-1] -= 1
	for i in reserve:
		suits[i-1] += 1
	for i in range(n):
		if suits[i] == 0:
			if i-1 >= 0 and suits[i-1] == 2:
				suits[i-1] -= 1
				suits[i] += 1
			elif i+1 < n and suits[i+1] == 2:
				suits[i+1] -= 1
				suits[i] += 1
	for i in range(n):
		if suits[i] != 0:
			answer += 1
	return answer