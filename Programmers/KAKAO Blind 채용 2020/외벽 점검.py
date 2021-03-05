from itertools import permutations

def solution(n, weak, dist):
	answer = -1
	len_weak = len(weak)
	len_dist = len(dist)

	circle_weak = weak
	for i in range(len_weak - 1):
		circle_weak.append(n + weak[i])
	
	dist.sort(reverse=True)
	for i in range(len_weak):
		weaks = circle_weak[i : len_weak+i]
		print(":::: NOW WEAK:", weaks)		
		for members in permutations(dist, len_dist):
			print("NOW MEMBERS:", members)
			now_pos = 0

			for idx, member in enumerate(members):
				# print(f'now_pos: {now_pos}, idx: {idx}, member: {member}')

				if now_pos + 1 >= len_weak:
					if answer == -1:
						answer = idx + 1
						print("BINGO First!!!!", weaks, members, answer)
					break
				elif weak[now_pos] + member == weaks[now_pos + 1]:
					now_pos += 2
					continue
				elif weaks[now_pos] + member < weaks[now_pos + 1]:
					now_pos += 1
					continue
				else:
					m = member
					while m != 0 and weaks[now_pos] + m >= weaks[now_pos + 1]:
						m -= weaks[now_pos + 1] - weaks[now_pos]
						now_pos += 1
						if now_pos >= len_weak - 1:
							if answer == -1 or answer > idx + 1:
								answer = idx + 1
								print("BINGO Second!!!!", weaks, members, answer)
							break

	return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4])) # 2
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7])) # 1
