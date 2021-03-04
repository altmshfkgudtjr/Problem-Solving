# 스택/큐

def solution(bridge_length, weight, trucks):
	answer = 0
	bridge = [0] * (bridge_length)
	now = 0
	while 1:
		answer += 1
		now -= bridge[0]
		bridge.pop(0)
		if len(trucks) != 0 and now + trucks[0] <= weight:
			now += trucks[0]
			bridge.append(trucks.pop(0))
		else:
			bridge.append(0)
		if now == 0:
			break
	return answer