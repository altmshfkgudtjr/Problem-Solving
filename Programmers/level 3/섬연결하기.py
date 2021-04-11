# TODO 크루스칼 또는 프림 알고리즘으로 다시 풀어보기

class Union:
	def __init__(self, items):
		self.nodes = set(items)
		self.root = -1

def getRoot(unions, idx):
	while unions[idx].root != idx:
		idx = unions[idx].root
	return idx

def solution(n, costs):
	if n == 1:
		return 0
	
	answer = 0
	unions = []
	islands = [None for _ in range(n)]
	
	costs.sort(key=lambda x: x[2])

	for cost in costs:	# O(N)
		island1 = cost[0]
		island2 = cost[1]
		answer += cost[2]
		
		if islands[island1] is None and islands[island2] is None:
			union = Union([island1, island2])
			unions.append(union)
			union_idx = len(unions) - 1
			union.root = union_idx
			islands[island1] = union_idx
			islands[island2] = union_idx
			if len(union.nodes) == n: break
		elif islands[island1] is not None and islands[island2] is not None:
			union1_root_idx = getRoot(unions, islands[island1])
			union2_root_idx = getRoot(unions, islands[island2])
			
			if union1_root_idx == union2_root_idx:
				answer -= cost[2]
				continue

			union1_root = unions[union1_root_idx]
			union2_root = unions[union2_root_idx]
			union1_root.root = union2_root.root
			union2_root.nodes = union1_root.nodes | union2_root.nodes

			islands[island1] = union2_root.root
			if len(union2_root.nodes) == n: break
		elif islands[island1] is None:
			union2_root_idx = getRoot(unions, islands[island2])
			union2_root = unions[union2_root_idx]
			union2_root.nodes.add(island1)
			islands[island1] = union2_root.root
			if len(union2_root.nodes) == n: break
		else: # islands[island2] is None:
			union1_root_idx = getRoot(unions, islands[island1])
			union1_root = unions[union1_root_idx]
			union1_root.nodes.add(island2)
			islands[island2] = union1_root.root
			if len(union1_root.nodes) == n: break

	return answer

# print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) # 4

# print(solution(4, [[0,1,1],[0,2,5],[1,2,3],[1,3,5],[2,3,1]])) # 5

# print(solution(1, [[]])) # 0

# print(solution(5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]])) # 6

# print(solution(5, [[0, 1, 1], [2, 3, 1], [1, 2, 2], [3, 4, 100], [0, 4, 2]])) # 6

# print(solution(5, [[0,1,1],[3,4,1],[1,2,2],[2,3,4]])) # 8

# print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]])) # 9

# print(solution(4, [[0,1,1],[0,2,2],[2,3,1]])) # 4

print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]])) # 104