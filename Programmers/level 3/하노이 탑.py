def path(target, from_, to):
	return [from_, to]

def hanoi(target, from_, to, middle):
	l = []
	if target == 1:
		l.append(path(target, from_, to))
	else:
		l += hanoi(target-1, from_, middle, to)
		l.append(path(target, from_, to))
		l += hanoi(target-1, middle, to, from_)
	return l

def solution(n):
	answer = hanoi(n, 1, 3, 2)
	return answer

print(solution(2)) # [[1,2], [1,3], [2,3]]