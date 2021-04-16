def solution(absolutes, signs):
	answer = 0
	for n, s in zip(absolutes, signs):
		if s:
			answer += n
		else:
			answer -= n	
	
	return answer


print(solution([4,7,12], [True, False, True]))
print(solution([1,2,3], [False, False, True]))