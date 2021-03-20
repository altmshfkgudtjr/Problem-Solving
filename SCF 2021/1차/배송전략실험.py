# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
path = list(input())
way = [1 for i in range(n)]
output = 1

# 초기 연속 1 1
piv_flag = 2

for i in range(n):
	if (path[i] == '0'):
		piv_flag = 2
		output *= way[i - 1]
		continue
	
	if piv_flag > 0:
		piv_flag -= 1
		continue

	way[i] = way[i - 1] + way[i - 2]

output *= way[i]

print(output)