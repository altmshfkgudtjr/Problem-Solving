def moveUp(table, now, cnt):
	while cnt > 0 and now > 0:
		now -= 1
		if table[now][1] == True:
			cnt -= 1
	return now

def moveDown(table, now, cnt, table_length):
	while cnt > 0 and now < table_length - 1:
		now += 1
		if table[now][1] == True:
			cnt -= 1
	return now

def cancelCell(table, now, table_length):
	table[now][1] = False
	origin_now = now
	flag = False
	isDown = True
	while not flag:
		if now == table_length - 1:
			isDown = False
			now = origin_now
		if isDown:
			now += 1
			flag = table[now][1]
		elif not isDown and now > 0:
			now -= 1
			flag = table[now][1]
	return now
	

def solution(n, k, cmds):
	table = [[_, True] for _ in range(n)]
	buffer = []

	for cmd in cmds:
		command = cmd.split()
		
		if command[0] == 'U':
			k = moveUp(table, k, int(command[1]))
		elif command[0] == 'D':
			k = moveDown(table, k, int(command[1]), n)
		elif command[0] == 'C':
			buffer.append(k)
			k = cancelCell(table, k, n)
		elif command[0] == 'Z':
			last = buffer.pop()
			table[last][1] = True

	result = list(map(lambda x: 'O' if x[1] else 'X', table))
	return ''.join(result)

print(solution(8, 2, ["C", "C", "C", "C", "C", "C", "C"])) # OOOOXOOO
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])) # OOOOXOOO
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])) # OOXOXOOO
