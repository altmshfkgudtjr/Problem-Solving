def solution(s):
	answer = []
	output = []
	for t in s[2:len(s)-2].split("},{"):
		tuples = []
		k = ''
		for i in list(t):
			if i != ',':
				k+=i
			else:
				tuples.append(int(k))
				k = ''
		tuples.append(int(k))
		output.append(tuples)
	output.sort(key=len)
	for o in output:
		o = list(filter(lambda x: x not in answer, o))
		answer.append(o[0])
	return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))