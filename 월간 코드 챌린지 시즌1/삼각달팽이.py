def solution(n):
	if n == 1:
		return [1]

	t = []
	for i in range(1, n + 1):
		t.append([0] * (i))

	cnt = n*(n+1)/2
	p = 1
	x = 0
	y = 0

	while p <= cnt:
		while y < n and t[y][x] == 0:
			t[y][x] = p
			p += 1
			y += 1
		y -= 1
		x += 1

		while x < n and t[y][x] == 0:
			t[y][x] = p
			p += 1
			x += 1
		x -= 2
		y -= 1

		while t[y][x] == 0:
			t[y][x] = p
			p += 1
			x -= 1
			y -= 1
			if t[y][x] != 0:
				break
		x += 1
		y += 2

	answer = []
	for i in range(n):
		answer += t[i]

	return answer