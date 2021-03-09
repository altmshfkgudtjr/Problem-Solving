from collections import deque

def solution(progresses, speeds):
	answer = deque([])

	time = list(map(lambda x: 
		(100 - x[1]) // speeds[x[0]] + 1 
		if (100 - x[1]) % speeds[x[0]] > 0 else 
		(100 - x[1]) // speeds[x[0]]
	, enumerate(progresses)))

	idx = len(time) - 1
	cnt = 0	
	while time:
		cnt += 1
		if not list(filter(lambda x: x >= time[idx], time[:idx])):
			answer.appendleft(cnt)
			cnt = 0
		idx -= 1
		time.pop()
		
	return list(answer)

print(solution([93,30,55], [1,30,5]))
# 7 3 9
# [2,1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# 5 10 1 1 20 1
# [1,3,2]
print(solution([99,99,99,99,99,99], [1,1,1,1,1,1]))
# 1 1 1 1 1 1
# [6]
print(solution([99,99,99,99,99,90], [1,1,1,1,1,1]))
# 1 1 1 1 1 10
# [5, 1]
print(solution([99,99,98,99,99,99], [1,1,1,1,1,1]))
# 1 1 2 1 1 1
# [2, 4]
print(solution([96,99,98,97], [1,1,1,1]))
# 4 1 2 3
# [4]