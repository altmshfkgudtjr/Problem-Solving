# 정렬

def solution(numbers):
	answer = ''
	numbers = list(map(str, numbers))
	List = []
	for num in numbers:
		output = num
		i = 0
		while len(output) < 4:
			output += num[i%len(num)]
			i+=1
		List.append({'origin': num, 'four': output})
	List.sort(reverse=True, key=lambda x: x['four'])
	for L in List:
		answer += L['origin']
	answer = str(int(answer))
	return answer