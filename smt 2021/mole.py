n = int(input())
scores = []
play_time = 0
for i in range(0, n**2):
	data = list(map(int, input().split()))
	score = {}
	score['score'] = data[0]
	score['time'] = data[2:]
	scores.append(score)
	t = int(data[len(data) - 1])
	if t > play_time:
		play_time = t

scores.sort(key=lambda x : x['score'], reverse=True)

output = 0
while play_time != 0:
	for score in scores:
		if play_time in score['time']:
			output += score['score']
			break	
	play_time -= 1

print(output)

'''
:::: 입력값 ::::

2
1 3 1 3 5
2 2 2 4
3 2 1 2
4 1 3
'''

"""
:::: 설명 ::::

다음과 같이 초기설정을 세팅해준다.
- 아래 리스트는 'score' 를 key값으로 내림차순 정렬된 상태이다.

scores = [
	{
		'score': '4',
		'time: [ 3 ]
	},
	{
		'score': '3',
		'time: [ 1, 2 ]
	},
	{
		'score': '2',
		'time: [ 2, 4 ]
	},
	{
		'score': '1',
		'time: [ 1, 3, 5 ]
	}
]

그리고 입력값에서 가장 최대 두더지 출현 시간을 기준으로 1씩 감소시키면서 최대 점수를 더해간다.

"""