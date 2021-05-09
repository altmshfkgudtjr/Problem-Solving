# from heapq import heappush, heappop

# def solution(t, r):
# 	answer = []
# 	customers = []
# 	customers_len = len(t)
# 	waits = []
# 	process = 0

# 	for idx, (time, grade) in enumerate(zip(t, r)):
# 		customers.append((idx, time, grade))
# 	customers.sort(key=lambda x: x[1], reverse=True)

# 	while waits or customers:
# 		while customers and customers[customers_len - 1][1] == process:
# 			customer = customers.pop()
# 			heappush(waits, (customer[2], customer))
# 			customers_len -= 1
		
# 		if waits:
# 			customer = heappop(waits)[1]
# 			answer.append(customer[0])
# 		process += 1

# 	return answer

def solution(t, r):
	answer = []
	customers = []
	customers_len = len(t)
	waits = []
	process = 0

	for idx, (time, grade) in enumerate(zip(t, r)):
		customers.append((idx, time, grade))
	customers.sort(key=lambda x: x[1], reverse=True)

	while waits or customers_len != 0:
		filtered = list(filter(lambda x: x[1] == process, customers))
		customers_len -= len(filtered)
		waits += filtered
		waits.sort(key=lambda x: (x[2], x[0]), reverse=True)
		if waits:
			customer = waits.pop()
			answer.append(customer[0])
		process += 1

	return answer


# 리프트 1초간격으로 들어옴
# t: 손님들 도착 시간
# r: 손님들 등급
# print(solution([0,1,3,0], [0,1,2,3])) # [0,1,3,2]
# print(solution([7,6,8,1], [0,1,2,3])) # [3,1,0,2]
# print(solution([0,0,0,0], [1,1,1,1])) # [0,1,2,3]
# print(solution([0,0,0,0,1,1,1,1], [2,2,2,2,1,1,1,0])) # [0, 7, 4, 5, 6, 1, 2, 3]
# print(solution([0,0,0,1,1,1,2,2,2,3,3,3], [4,4,4,5,5,5,0,0,0,1,1,1])) # [0, 1, 6, 7, 8, 9, 10, 11, 2, 3, 4, 5]
# print(solution([999,999,1000], [1,0,1])) # [1,0,2]
# print(solution([1,1,1,1,1,1,1,1], [5,4,3,2,1,5,4,3])) # []
print(solution([1,1,2,3,4], [5,4,3,2,1])) # [1, 2, 3, 4, 0]
