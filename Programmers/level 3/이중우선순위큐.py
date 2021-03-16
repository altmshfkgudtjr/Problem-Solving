from heapq import heappush, heappop

def solution(operations):
	heap = []
	heap_len = 0

	for op in operations:
		cmd, val = op.split()
		
		if cmd == 'I':
			heappush(heap, int(val))
			heap_len += 1
		elif cmd == 'D':
			if heap_len == 0:
				continue
			if val == '-1':
				heappop(heap)
			else:
				m = max(heap)
				heap.remove(m)
			heap_len -= 1
			
	if heap_len == 0:
		return [0, 0]
	return [max(heap), heappop(heap)]


print(solution(["I 16","D 1"]), [0,0])
print(solution(["I 7","I 5","I -5","D -1"]), [7,5])