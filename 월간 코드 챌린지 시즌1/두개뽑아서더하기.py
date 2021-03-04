def solution(numbers):
	answer = []

	for i, a in enumerate(numbers):
		for j, b in enumerate(numbers):
			if i == j:
				continue
			if a + b not in answer:
				answer.append(a + b)

	return sorted(answer)