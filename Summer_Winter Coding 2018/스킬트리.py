def solution(skill, skill_trees):
	answer = 0
	skill_set = set(skill)
	
	for s in skill_trees:
		flag = True
		idx = 0
		for c in s:
			if c not in skill_set:
				continue
			t = skill.index(c)
			if t != idx:
				flag = False
				break
			else:
				idx += 1
		if flag:
			answer += 1
			
	return answer
