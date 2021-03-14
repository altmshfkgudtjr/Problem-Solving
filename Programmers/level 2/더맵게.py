import heapq

def solution(scoville, K):
	count = 0

	if min(scoville) >= K:
		return 0

	heap_len = len(scoville)
	heapq.heapify(scoville)
	while heap_len >= 2:
		a = heapq.heappop(scoville)
		b = heapq.heappop(scoville)
		c = a + (b * 2)
		
		heap_len -= 2
		count += 1
	
		if heap_len == 0 and c < K:
			return -1
		if (heap_len == 0 and c >= K) or (scoville[0] >= K and c >= K):
			return count
		else:
			heapq.heappush(scoville, c)
			heap_len += 1

	return -1

print(solution([1,2,3,9,10,12], 7)) # 2

"""
"제일 작은 값 + (다음 제일 작은 값 * 2)" 과정을 지속하여 모든 값이 K가 넘으면 되는 조건이다.

# Key Point
이 때, 반복문을 돌면서 배열의 길이를 구하는 것은 연산낭비라고 생각하여 따로 변수로 빼주어 계산하였다.

"""