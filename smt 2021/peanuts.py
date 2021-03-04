n, m, e = list(map(int, input().split()))
positions = list(map(int, input().split()))

lpositions = []
rpositions = []

for p in positions:
	if p < e:
		lpositions.append(p)
	else:
		rpositions.append(p)
lpositions.reverse()

l_idx = 0
r_idx = 0
l = e - lpositions[l_idx]
r = rpositions[r_idx] - e
length = 0

while m != 0:
	if l < r:
		length += l
		l_idx += 1
		if l_idx >= len(lpositions):
  			l = 10001
		else:
			l = lpositions[l_idx-1] - lpositions[l_idx]
	else:
		length += r
		r_idx += 1
		if r_idx >= len(rpositions):
  			r = 100001
		else:
			r = rpositions[r_idx] - rpositions[r_idx-1]
	m -= 1

print(length)

'''
:::: 입력값 ::::

6 3 7
2 4 5 8 11 12
'''


"""
:::: 설명 ::::

아래와 같이 초기 설정을 마친다.

lpositions: [ 5, 4, 2 ]
rpositions: [ 8, 11, 12 ]

그 다음 각 변수의 변화 과정은 다음과 같다.

m	l_idx	r_idx	l		r		length
3	0		0		2		1		0 -> 1
2	0		1		2		3		1 -> 3
1	1		1		1		3		3 -> 4
0	END		END		END		END		4

만약 배열의 끝에 도달하면 땅콩의 최대갯수보다 큰 10001을 넣어주어서 해당 방향으로 향하지 않도록 하였다.
"""