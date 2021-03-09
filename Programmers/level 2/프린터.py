from collections import deque

def solution(priorities, location):
	answer = 0
	indexes = deque([i for i in range(len(priorities))])
	waits = deque(priorities)

	while len(waits) != 0:
		target = waits.popleft()
		target_idx = indexes.popleft()
		if len(list(filter(lambda x: x > target, waits))):
			waits.append(target)
			indexes.append(target_idx)
			continue
		else:
			answer += 1
		
		if target_idx == location:
			break

	return answer
 

print(solution([2,1,3,2], 2)) # 1
print(solution([2,1,3,2], 3)) # 2
print(solution([1,1,9,1,1,1], 0)) # 5
print(solution([1,1,9,1,1,1], 5)) # 4