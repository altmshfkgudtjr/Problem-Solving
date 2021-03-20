# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, m = map(int, input().split())
clothes = []
basket = [[0]*n for _ in range(m)]

for i in range(m):
	clothes.append(list(map(int, input().split())))

basket[0][0] = clothes[0][0]

# 세로 0번째줄 초기화
for i in range(1, m):
	basket[i][0] = basket[i - 1][0] + clothes[i][0]

# 가로 0번째줄 초기화
for i in range(1, n):
	basket[0][i] = basket[0][i - 1] + clothes[0][i]


for i in range(1, m):
	for j in range(1, n):
		top_cnt = basket[i - 1][j] + clothes[i][j]
		left_cnt = basket[i][j - 1] + clothes[i][j]
		basket[i][j] = max(top_cnt, left_cnt)

print(basket[m - 1][n - 1])

"""
3 5
3 4 5
2 3 9
3 9 3
4 5 1
1 3 6
"""