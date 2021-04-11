def solution(routes):
	answer = 0
	routes.sort(key=lambda x: x[0])
	p_s = routes[0][0]
	p_e = routes[0][1]

	for route in routes[1:]:
		p_s = route[0]
		if route[1] < p_e:
			p_e = route[1]
		if p_s > p_e:
			answer += 1
			p_e = route[1]
	answer += 1
	
	return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) # 2