from heapq import heapify, heappush, heappop

def solution(jobs):
	jobs_len = len(jobs)
	time = 0
	pendding = 0
	waits = []
	heapify(jobs)

	while jobs or waits:
		# 대기하는 Job들 중에서 가장 효율적인 Job 선택
		if waits:
			min_idx = 0
			for i in range(1, len(waits)):
				if waits[min_idx][1] > waits[i][1]:
					min_idx = i
			start, running_time = waits.pop(min_idx)
		else:
			time = jobs[0][0]
			start, running_time = heappop(jobs)

		pendding += time - start + running_time
		time += running_time
		
		# 진행하고 있는 도중에 요청이 온 Job들 추출
		while jobs and jobs[0][0] <= time:
			heappush(waits, heappop(jobs))

	return pendding // jobs_len


print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[1000, 1000]]), 1000)
print(solution([[0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [1000, 1000]]), 500)
print(solution([[100, 100], [1000, 1000]]), 550)
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72) # Error!
print(solution([[0,20],[3,4],[3,5],[17,2]]), 19)
print(solution([[0,1],[0,1],[1,0]]), 1)