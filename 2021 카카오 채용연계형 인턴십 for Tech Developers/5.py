# TODO 문제 다시 풀기

from collections import deque

class Room:
	def __init__(self, idx, left, right, cnt):
		self.idx = idx
		self.parent = None
		self.left = left if left != -1 else None
		self.right = right if right != -1 else None
		self.cnt = cnt
	def printInfo(self):
		print(
			self.idx,
			self.parent.idx if self.parent else None,
			self.left.idx if self.left else None, 
			self.right.idx if self.right else None,
			self.cnt
		)

def making_level_circuit(root):
	deq = deque()
	stack = []

	deq.appendleft(root)
	while deq:
		room = deq.pop()
		stack.append(room)
		if room.right:
			deq.appendleft(room.right)
		if room.left:
			deq.appendleft(room.left)
	stack.reverse()
	return stack
	

def solution(k, num, links):
	max_cnt = 0
	avg = sum(num)//k
	rooms = []
	for idx, (cnt, [left, right]) in enumerate(zip(num, links)):
		rooms.append(Room(idx, left, right, cnt))

	for room in rooms:
		left_idx = room.left
		right_idx = room.right
		if left_idx != None:
			rooms[left_idx].parent = room
			room.left = rooms[left_idx]
		if right_idx != None:
			rooms[right_idx].parent = room
			room.right = rooms[right_idx]
	
	root = list(filter(lambda x: x.parent == None, rooms))[0]
	level_circuit = making_level_circuit(root)

	for room in level_circuit:
		if room.cnt >= avg:
			if max_cnt < room.cnt:
				max_cnt = room.cnt
		elif room.parent == None:
			pass
		else:
			room.parent.cnt += room.cnt

	return sum(num) if max_cnt == 0 else max_cnt



# 40
print(solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))

# 27
print(solution(1, [6, 9, 7 ,5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))

# 14
print(solution(2, [6, 9, 7 ,5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))

# 9
print(solution(4, [6, 9, 7 ,5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))