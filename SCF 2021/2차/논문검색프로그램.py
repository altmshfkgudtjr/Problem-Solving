# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import re

n = int(input())
words = [input() for _ in range(n)]
q = int(input())
keywords = [input() for _ in range(q)]

for keyword in keywords:
	cnt = 0
	for word in words:
		if re.search(keyword, word) is not None:
			cnt += 1
	print(cnt)

"""
5
dijkstra
greedy
bfs
backtracking
dynamic
3
bfs
greedyalgorithm
ra
"""