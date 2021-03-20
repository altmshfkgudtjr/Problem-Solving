# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import defaultdict

genre_char = ['A', 'B', 'C', 'D', 'E']
score_input = list(map(float, input().split()))
score = defaultdict(float)
for idx, c in enumerate(genre_char):
	score[c] = score_input[idx]

n, m = map(int, input().split())

Y = []
O = []
genre = []

for i in range(n):
	t = list(input())
	for j in range(m):
		if t[j] == 'Y':
			Y.append((i, j))
		elif t[j] == 'O':
			O.append((i, j))

for i in range(n):
	genre.append(list(input()))

tmp = []
for pos in Y:
	tmp.append([genre[pos[0]][pos[1]], pos])
Y = tmp

tmp = []
for pos in O:
	tmp.append([genre[pos[0]][pos[1]], pos])
O = tmp

Y.sort(key=lambda x: x[1][1])
Y.sort(key=lambda x: x[1][0])
Y.sort(key=lambda x: score[x[0]], reverse=True)

O.sort(key=lambda x: x[1][1])
O.sort(key=lambda x: x[1][0])
O.sort(key=lambda x: score[x[0]], reverse=True)

for y in Y:
	print(f'{y[0]} {score[y[0]]} {y[1][0]} {y[1][1]}')
for o in O:
	print(f'{o[0]} {score[o[0]]} {o[1][0]} {o[1][1]}')

"""
4.0 3.0 2.1 4.3 5.0
2 3
WYO
YYO
ABC
DCE
"""