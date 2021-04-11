# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from heapq import heappush, heappop

class Place:
	def __init__(self, name):
		self.name = name
		self.connection = []
		self.check = False
	def connect(self, edge):
		self.connection.append(edge)
	def	visit(self):
		self.check = True

class Edge:
	def __init__(self, place1, place2, weight, idx):
		self.place1 = place1
		self.place2 = place2
		self.weight = weight
		self.check = False
		self.done = False
		self.idx = idx
	def bag(self):
		self.check = True
	def finish(self):
		self.done = True

n = int(input())
placeList = []
edgeList = []
resource = 0

for i in range(n):
	P1 = None
	P2 = None
	p1, p2, weight = input().split()

	isP1 = list(filter(lambda x: x.name == p1, placeList))
	if len(isP1) == 0:
		P1 = Place(p1)
		placeList.append(P1)
	else:
		P1 = isP1[0]

	isP2 = list(filter(lambda x: x.name == p2, placeList))
	if len(isP2) == 0:
		P2 = Place(p2)
		placeList.append(P2)
	else:
		P2 = isP2[0]

	E = Edge(P1, P2, int(weight), i)
	edgeList.append(E)
	P1.connect(E)
	P2.connect(E)

# Prim 알고리즘
P = placeList[0]
P.visit()
heap = []
check_cnt = 1

while check_cnt < len(placeList):
	for e in P.connection:
		if not e.check and not e.done:
			heappush(heap, (e.weight, e.idx, e))
			e.bag()
	[ weight, _, E ] = heappop(heap)
	E.finish()
	P = E.place2 if E.place1.check else E.place1
	P.visit()
	check_cnt += 1
	resource += E.weight


# Kruskal 알고리즘

# edgeList.sort(key=lambda x: x.weight)
# for edge in edgeList:
# 	P1 = edge.place1
# 	P2 = edge.place2
	
# 	if P1.check and P2.check:
# 		continue
	
# 	P1.visit()
# 	P2.visit()
# 	resource += edge.weight


print(resource)



"""12
6
A B 3
B C 10
A D 4
A C 6
D C 5
B D 5
"""

"""12
8
a b 1
b c 2
c d 2
d e 4
e f 4
f a 9
a d 8
a e 3
"""