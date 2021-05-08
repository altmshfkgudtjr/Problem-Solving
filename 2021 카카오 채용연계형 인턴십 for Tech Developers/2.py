# First Check
def checkLine(place, row, col):
	# 1 block
	if row > 0 and place[row - 1][col] == 'P':
		return False
	if row < 4 and place[row + 1][col] == 'P':
		return False
	if col > 0 and place[row][col - 1] == 'P':
		return False
	if col < 4 and place[row][col + 1] == 'P':
		return False

	# 2 block
	if row > 0 and place[row - 1][col] == 'O':
		if row > 1 and place[row - 2][col] == 'P':
			return False
	if row < 4 and place[row + 1][col] == 'O':
		if row < 3 and place[row + 2][col] == 'P':
			return False
	if col > 0 and place[row][col - 1] == 'O':
		if col > 1 and place[row][col - 2] == 'P':
			return False
	if col < 4 and place[row][col + 1] == 'O':
		if col < 3 and place[row][col + 2] == 'P':
			return False
	return True

# Second Check
def checkDiagonal(place, row, col):
	if row > 0 and col > 0 and place[row - 1][col - 1] == 'P':
		if place[row - 1][col] == 'O' or place[row][col - 1] == 'O':
			return False
	if row < 4 and col > 0 and place[row + 1][col - 1] == 'P':
		if place[row + 1][col] == 'O' or place[row][col - 1] == 'O':
			return False
	if row > 0 and col < 4 and place[row - 1][col + 1] == 'P':
		if place[row - 1][col] == 'O' or place[row][col + 1] == 'O':
			return False
	if row < 4 and col < 4 and place[row + 1][col + 1] == 'P':
		if place[row + 1][col] == 'O' or place[row][col + 1] == 'O':
			return False
	return True

def checkPlace(place):
	members = []

	# get members position
	for row, place_row in enumerate(place):
		for col, val in enumerate(place_row):
			if val == "P":
				members.append((row, col))
	
	for member in members:
		if checkLine(place, member[0], member[1]):
			if checkDiagonal(place, member[0], member[1]):
				continue
			else:
				return 0
		else:
			return 0
	return 1

def solution(places):
	answer = []

	for place in places:
		answer.append(checkPlace(place))
	
	return answer

input_places = [
	[
		"POOOP", 
		"OXXOX", 
		"OPXPX", 
		"OOXOX", 
		"POXXP"
	], 
	[
		"POOPX", 
		"OXPXP", 
		"PXXXO", 
		"OXXXO", 
		"OOOPP"
	], 
	[
		"PXOPX", 
		"OXOXP", 
		"OXPXX", 
		"OXXXP", 
		"POOXX"
	], 
	[
		"OOOXX", 
		"XOOOX", 
		"OOOXX", 
		"OXOOX", 
		"OOOOO"
	], 
	[
		"PXPXP", 
		"XPXPX", 
		"PXPXP", 
		"XPXPX", 
		"PXPXP"
	]
]
print(solution((input_places))) # [1, 0, 1, 1, 1]