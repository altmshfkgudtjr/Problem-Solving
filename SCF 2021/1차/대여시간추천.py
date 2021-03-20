# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
start = "00:00"
end = "23:59"

def time2value(time):
	[h, m] = time.split(':')
	return int(h) * 60 + int(m)

for i in range(n):
	[s, e] = input().split(' ~ ')
	if time2value(start) < time2value(s):
		start = s
	if time2value(end) > time2value(e):
		end = e

if time2value(start) > time2value(end):
	print("-1")
else:
	print(f'{start} ~ {end}')