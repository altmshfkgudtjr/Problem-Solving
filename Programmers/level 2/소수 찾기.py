# 완전탐색

from itertools import permutations

def Is_Prime(num):
	num = int(num)
	if num is 0 or num is 1:
		return False
	if num is 2:
		return True
	if num%2 is 0:
		return False
	for i in range(3, num, 2):
		if num%i is 0:
			return False
	return True

def solution(numbers):
	answer = []
	nums = list(numbers)
	for i in range(1, len(nums) + 1):
		p = list(set(list(permutations(nums, i))))
		for j in p:
			j = ''.join(list(j))
			if Is_Prime(j):
				answer.append(j)
	answer = len(set(list(map(int, answer))))
	return answer