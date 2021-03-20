# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import defaultdict

n = int(input())
room = []
total = 0
production = defaultdict(int)

for i in range(n):
	room.append(list(map(int, list(input()))))
	production[i + 1] = 0

for size in range(0, n + 1):
	for i in range(n - size):
		for j in range(n - size):
			target = [row[j:j+size + 1] for row in room[i:i+size + 1]]
			target = set(sum(target, []))
			if 0 not in target:
				total += 1
				production[size + 1] += 1

print(f'total: {total}')
for key in production.keys():
	if production[key] == 0:
		continue
	print(f'size[{key}]: {production[key]}')