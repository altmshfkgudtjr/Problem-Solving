class Ground:
	def __init__(self, idx, pos):
		self.idx = idx
		self.pos = pos
		self.check = False
		self.count = 0

n = int(input())
grounds = list(map(int, input().split()))
grounds = [Ground(idx, pos) for idx, pos in enumerate(grounds)]

# 발판 밟는 함수
def check_ground(ground, count):
	# print("들어옴:", ground.idx, ground.pos, ", 카운트:", count)
	if ground.check:
		if ground.count != 0:
			return ground.count
		ground.count = count
		return 1

	ground.check = True
	result = check_ground(grounds[ground.idx + ground.pos], count + 1)
	ground.count = result + 1
	return result + 1

# 디버그용 출력함수
def print_ground():
	print("현재: ", end="")
	for ground in grounds:
		print(ground.count, end=" ")
	print()

output_list = []
for i in range(0, 3):
	result = check_ground(grounds[i], 1)
	output_list.append(result)
	# print_ground()

print(max(output_list))


'''
:::: 입력값 ::::

10
3 5 -1 -2 4 4 3 -2 -3 -2
'''

"""
:::: 설명 ::::

본 알고리즘은 다음과 같이 진행된다.

<1번 발판>
		1	2	3	4	5	6	7	8	9	10
Check	T	F	F	F	F	F	F	F	F	F	
Count	0	0	0	0	0	0	0	0	0	0

Check	T	F	F	T	F	F	F	F	F	F	
Count	0	0	0	0	0	0	0	0	0	0

Check	T	T	F	T	F	F	F	F	F	F
Count	0	0	0	0	0	0	0	0	0	0

Check	T	T	F	T	F	F	T	F	F	F
Count	0	0	0	0	0	0	0	0	0	0

Check	T	T	F	T	F	F	T	F	F	T
Count	0	0	0	0	0	0	0	0	0	0

Check	T	T	F	T	F	F	T	T	F	T
Count	0	0	0	0	0	0	0	0	0	0

Check	T	T	F	T	F	T	T	T	F	T
Count	0	0	0	0	0	0	0	0	0	0

Check	T	T	F	T	F	T	T	T	F	T!	=> 밟았던 10번째 발판을 다시 밟게 된다.
Count	0	0	0	0	0	0	0	0	0	0

Check	T	T	F	T	F	T	T	T	F	T	=> Count를 1씩 증가하면서 재귀를 반환한다. (과정 생략)
Count	8	6	0	7	0	2	5	3	0	4

반환: 8


<2번 발판>

Check	T	T!	F	T	F	T	T	T	F	T	=> 처음부터 이미 구했던 발판이 존재하므로 바로 Return 한다.
Count	8	6	0	7	0	2	5	3	0	4

반환: 6


<3번 발판>

Check	T	T	T	T	F	T	T	T	F	T
Count	8	6	0	7	0	2	5	3	0	4

Check	T	T!	T	T	F	T	T	T	F	T	=> 밟았던 발판부터 Count를 Return 한다.
Count	8	6	0	7	0	2	5	3	0	4

Check	T	T	T	T	F	T	T	T	F	T
Count	8	6	7	7	0	2	5	3	0	4

반환: 7


위 과정 결과 [ 8, 6, 7 ] 에서 가장 큰 값인 8이 출력된다.

"""