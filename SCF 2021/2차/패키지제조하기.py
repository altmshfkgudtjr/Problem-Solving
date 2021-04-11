# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
[n, q] = map(int, input().split())
parentList = [None for _ in range(n + 1)]

for i in range(n - 1):
	[parent, child] = map(int, input().split())

	parentList[child] = parent

for i in range(q):
	flag = False
	[parent, child] = map(int, input().split())
	p = parentList[child]

	while p:
		if p == parent:
			flag = True
			break
		p = parentList[p]
	
	if flag:
		print("yes")
	else:
		print("no")


# 두 번째 방법
# [n, q] = map(int, input().split())
# parentList = [set([]) for _ in range(n + 1)]

# for i in range(n - 1):
# 	[parent, child] = map(int, input().split())
# 	parentList[child].add(parent)
# 	parentList[child] = parentList[child] | (parentList[parent])

# for parent in parentList:
# 	print(parent)

# for i in range(q):
# 	[parent, child] = map(int, input().split())
# 	if parent in parentList[child]:
# 		print('yes')
# 	else:
# 		print('no')

"""
6 6
6 4
6 5
4 1
4 2
4 3
1 4
4 1
6 5
1 6
6 3
4 3
"""


"""
13 2
4 1
4 2
4 3
5 6
5 7
5 8
10 4
10 5
11 5
11 9
12 11
12 10

7 9
7 11
"""