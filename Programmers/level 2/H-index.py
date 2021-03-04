# 정렬

def solution(docs):
	n = len(docs)
	for i in range(n + 1):
		if len(list(filter(lambda x: x >= n - i, docs))) >= n - i:
			return n - i