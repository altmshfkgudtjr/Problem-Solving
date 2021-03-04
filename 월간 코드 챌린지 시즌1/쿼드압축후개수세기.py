def solution(arr):
	if type(arr[0][0]) == 'int' and arr[0][0]:
		return [0, 1]
	elif type(arr[0][0]) == 'int':
		return [1, 0]
	answer = []

	s = arr[0][0]
	l = len(arr) // 2
	for line in arr:
		for n in line:
			if s != n:
				zero_1, one_1 = solution([arr[i][:l] for i in range(0,l)])
				zero_2, one_2 = solution([arr[i][:l] for i in range(l,l*2)])
				zero_3, one_3 = solution([arr[i][l:] for i in range(0,l)])
				zero_4, one_4 = solution([arr[i][l:] for i in range(l,l*2)])
				return [zero_1+zero_2+zero_3+zero_4, one_1+one_2+one_3+one_4]
	if s:
		return [0, 1]
	return [1, 0]