def stackChecker(s):
	stack = []
	for c in s:
		if c == '(' or c == '{' or c == '[':
			stack.append(c)
		else:
			if len(stack) == 0:
				return False
			tmp = stack.pop()
			if (tmp == '(' and c == ')') or\
				(tmp == '{' and c == '}') or\
				(tmp == '[' and c == ']'):
				pass
			else:
				stack.append(tmp)
				stack.append(c)

	if len(stack) > 0:
		return False
	return True
				

def solution(s):
	answer = 0
	s_len = len(s)
	
	for i in range(s_len):
		if stackChecker(s[i:] + s[:i]):
			answer += 1

	return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))