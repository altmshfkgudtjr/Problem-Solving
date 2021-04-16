class Node:
	def __init__(self, number, weight):
		self.number = number
		self.weight = weight
		self.connections = []
		self.parent = self

# 재귀 방식: 4개 틀렸다고 나오지만 런타임에러 아마도 메모리 초과
# def postorder(root, parent, nodes):
# 	prev_cnt = 0
# 	for n in root.connections:
# 		if n != parent:
# 			prev_cnt += postorder(nodes[n], root.number, nodes)
	
# 	cnt = root.weight
# 	nodes[parent].weight += cnt
# 	root.weight = 0

# 	return abs(cnt) + prev_cnt
	

# def solution(a, edges):
# 	if sum(a) != 0:
# 		return -1

# 	nodes = [Node(i, a[i]) for i in range(len(a))]

# 	for edge in edges:
# 		nodes[edge[0]].connections.append(edge[1])
# 		nodes[edge[1]].connections.append(edge[0])

# 	answer = postorder(nodes[0], -1, nodes)

# 	return answer

# 큐버젼, 8개 틀리고 그냥 시간초과
def solution(a, edges):
	if sum(a) != 0:
		return -1

	nodes = [Node(i, a[i]) for i in range(len(a))]

	for edge in edges:
		nodes[edge[0]].connections.append(edge[1])
		nodes[edge[1]].connections.append(edge[0])

	q1 = [nodes[0]]
	q2 = []
	checker = set([])

	while q1:
		node = q1.pop()
		q2.append(node.number)
		checker.add(node.number)

		for n in node.connections:
			if n not in checker:
				nodes[n].parent = node
				q1.append(nodes[n])
	
	q2.reverse()

	answer = 0
	
	for n in q2:
		cnt = nodes[n].weight
		nodes[n].parent.weight += cnt
		
		answer += abs(cnt)

	return answer

print(solution([1,-7,0,4,-2,4], [[0,5],[1,5],[1,2],[4,5],[3,4]])) # 14
print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
print(solution([0,1,0], [[0,1],[1,2]])) # -1