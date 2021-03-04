def solution(s):
	answer = [0, 0]

	while s != '1':
		n = s.count('0')
		s = s.replace('0', '')
		s = bin(len(s))[2:]

		answer = [answer[0]+1, answer[1]+n]

	return answer