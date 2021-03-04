import collections

p, n, h = input().split()
n = int(n)
h = int(h)

pc_user = collections.defaultdict(list)

for i in range(0, n):
	pc, user = input().split()
	user = int(user)

	pc_user[pc]
	if (user <= h):
		pc_user[pc].append(user)

# 배낭 알고리즘
def knapSack(W , wt , val, n): 
	if n == 0 or W == 0 : 
		return 0
	if (wt[n-1] > W): 
		return knapSack(W , wt , val , n-1) 
	else: 
		return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
					knapSack(W , wt , val , n-1))

for pc in pc_user.keys():
	money = 0
	hour = knapSack(h, pc_user[pc], pc_user[pc], len(pc_user[pc]))
	money += hour * 1000
	
	print(f'{pc} {money}')


'''
:::: 입력값 ::::

2 7 10
1 10
1 5
1 7
2 10
2 1
2 3
2 7
'''

"""
:::: 설명 ::::

초반에 운영시간 h 보다 작은 시간을 전부 입력받아 다음과 같이 설정한다.
pc_user: {
	'1': [10, 5, 7],
	'2': [10, 1, 3, 7]
}

각 pc 번호에 대한 배열에서 '배낭 알고리즘'을 통해서 가능한 N 미만의 최대 합을 구한다.

"""