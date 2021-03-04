def solution(board, moves):
	answer = 0
	stack = []
	for move in moves:
		move -= 1
		catch = None
		for row in board:
			if row[move] == 0:
				continue
			catch = row[move]
			row[move] = 0
			break
		if catch != None:
			if len(stack) != 0 and stack[len(stack)-1] == catch:
				stack.pop()
				answer+=1
			else:
				stack.append(catch)
	return answer*2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

'''
0 0 0 0 0
0 0 1 0 3
0 2 5 0 1
4 2 4 4 2
3 5 1 3 1

1 5 3 5 1 2 1 4
---------------
4 3 1 1 3 2 x 4
4 3 3 2 x 4
4 2 x 4
'''