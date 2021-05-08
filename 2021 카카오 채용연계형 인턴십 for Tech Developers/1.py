def solution(s):
	table = {
		'zero': '0',
		'one': '1',
		'two': '2',
		'three': '3',
		'four': '4',
		'five': '5',
		'six': '6',
		'seven': '7',
		'eight': '8',
		'nine': '9',
	}
	answer = ""
	stack = ""
	for c in s:
		if '0' <= c and c <= '9':
			answer += c
		elif stack in table:
			answer += table[stack]
			stack = ""
		else:
			stack += c
			if stack in table:
				answer += table[stack]
				stack = ""
	return int(answer)

print(solution(("one4seveneight"))) # 1478
print(solution(("23four5six7"))) # 234567
print(solution(("2three45sixseven"))) # 234567
print(solution(("123"))) # 123