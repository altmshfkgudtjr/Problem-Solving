# 완전탐색

def solution(answers):
	answer = [1,2,3]
	students = []
	students.append([1,2,3,4,5])
	students.append([2,1,2,3,2,4,2,5])
	students.append([3,3,1,1,2,2,4,4,5,5])
	output = []
	for st in range(len(students)):
		num = 0
		st_len = len(students[st])
		for i in range(len(answers)):
			if answers[i] == students[st][i % st_len]:
				num += 1
		students[st] = num
	a = max(students)
	for i in range(3):
		if students[i] == a:
			output.append(answer[i])
	return output