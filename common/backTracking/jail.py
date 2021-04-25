import time

col_len = 0
row_len = 0
max_cnt = 0
case_cnt = 0
previewJail = []

def bindingCriminal(idx, row):
	global row_len

	row[idx] = 'V'
	for i in range(idx-1, -1, -1):
		if row[i] != '#':
			row[i] = 'X'
		else:
			break
	for i in range(idx+1, row_len):
		if row[i] != '#':
			row[i] = 'X'
		else:
			break

def checker(row, row_idx, col_idx, criminal_cnt):
	global jail
	global row_len
	global col_len
	global max_cnt
	global case_cnt

	global previewJail
	
	if row_idx == row_len and col_idx == col_len - 1:
		previewJail[col_idx] = row

		# 전체 끝 -> 경우의 수 1개 완료
		if max_cnt < criminal_cnt:
			max_cnt = criminal_cnt
			case_cnt = 1
		elif max_cnt == criminal_cnt:
			case_cnt += 1
	elif row_idx == row_len:
		previewJail[col_idx] = row
		
		# 한줄 끝 -> 세로로 이동
		next_row = []
		for i in range(row_len):
			if jail[col_idx + 1][i] == 'O':
				# 다음 줄이 "O" 일 때
				if row[i] == 'V':
					# 현재 줄이 "V" 일 떄
					next_row += ['X']
				elif row[i] == 'X':
					# 현재 줄이 "X" 일 때
					for j in range(col_idx - 1, -1, -1):
						if previewJail[j][i] == '#':
							next_row += [jail[col_idx + 1][i]]
							break
						# "X"가 y축에서 온 것인지 체크
						if previewJail[j][i] == 'V':
							next_row += ['X']
							break
					else:
						# y축에서 온 것이 아니라면 다음라인 그대로 추가
						next_row += [jail[col_idx + 1][i]]
				else:
					# 현재 줄이 "O" 일 때
					next_row += [jail[col_idx + 1][i]]
			else:
				# 다음 줄이 "O"가 아닐 때
				next_row += [jail[col_idx + 1][i]]
		checker(next_row, 0, col_idx + 1, criminal_cnt)
	else:
		# 진행 중 -> 가로로 이동
		if row[row_idx] != 'O':
			# 수감하지 못함
			checker(row[:], row_idx + 1, col_idx, criminal_cnt)
		else:
			# 수감하지 않음
			checker(row[:], row_idx + 1, col_idx, criminal_cnt)
			# 수감함
			temp = row[:]
			bindingCriminal(row_idx, temp)
			checker(temp, row_idx + 1, col_idx, criminal_cnt + 1)

def solution(jail):
	global col_len
	global row_len
	global max_cnt
	global case_cnt
	global previewJail

	col_len = len(jail)
	row_len = len(jail[0])

	previewJail = [[0 for _ in range(row_len)] for _ in range(col_len)]
	
	checker([jail[0][_] for _ in range(row_len)], 0, 0, 0)
	
	return (max_cnt, case_cnt)



''' 
	벽 = # 
	길 = O
'''
# 최대 15명, 560가지
jail = [["O", "#", "O", "#", "O", "#", "O", "#"],
		["O", "O", "O", "O", "O", "#", "O", "O"],
		["#", "O", "#", "O", "O", "#", "O", "#"],
		["O", "O", "O", "O", "O", "O", "O", "O"],
		["O", "O", "O", "#", "O", "O", "O", "O"],
		["O", "O", "O", "O", "O", "#", "O", "#"],
		["O", "#", "O", "O", "O", "O", "O", "O"],
		["O", "O", "O", "O", "#", "O", "#", "O"]]
# 최대 4명, 2가지
# jail = [["#", "#", "#", "O"],
# 		["O", "O", "O", "O"],
# 		["O", "#", "O", "O"],
# 		["#", "#", "#", "O"]]
# 최대 6명, 720가지
jail = [["O", "O", "O", "O", "O", "O"],
		["O", "O", "O", "O", "O", "O"],
		["O", "O", "O", "O", "O", "O"],
		["O", "O", "O", "O", "O", "O"],
		["O", "O", "O", "O", "O", "O"],
		["O", "O", "O", "O", "O", "O"]]
# 최대 4명, 24가지
# jail = [["O", "O", "O", "O"],
# 		["O", "O", "O", "O"],
# 		["O", "O", "O", "O"],
# 		["O", "O", "O", "O"]]
# 최대 3명, 6가지
# jail = [["O", "O", "O"],
# 		["O", "O", "O"],
# 		["O", "O", "O"]]
# 최대 2명, 2가지
# jail = [["O", "O"],
# 		["O", "O"]]
# 최대 9명, 33가지
# jail = [["O","O","O","#","O","O","O","O"],
# 		["O","O","O","O","O","#","O","#"],
# 		["O","#","O","O","O","O","O","O"],
# 		["O","O","O","O","#","O","#","O"]]

start_time = time.time()
print(solution(jail))
print(f'time: {time.time()-start_time}')