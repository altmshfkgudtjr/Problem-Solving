from collections import deque

# 인원 제한 ㅌ
def solution(people, limit):
	answer = 0
	cnt = 0
	people.sort()
	people = deque(people)
	
	while people:
		cnt += people.pop()
		while cnt <= limit:
			if people and cnt + people[0] <= limit:
				cnt += people.popleft()
			else:
				answer += 1
				cnt = 0
				break

	return answer


print(solution([70,50,80,50], 100)) # 3

print(solution([70,80,50], 100)) # 3

print(solution([10,20,10,20,30], 30)) # 3

print(solution([10,10,10,20,40], 40)) # 3

print(solution([10,10,20,20], 40)) # 2

print(solution([10,10,20,40], 40)) # 2


# 한 번에 2명씩 제한
def solution_(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer

print(solution_([10,10,20,40], 40)) # 3