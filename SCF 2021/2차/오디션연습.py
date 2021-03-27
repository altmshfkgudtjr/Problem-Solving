# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from heapq import heappush, heappop

def time2second_1(time):
	[h, m, s] = map(int, time.split(':'))
	return h * 360 + m * 60 + s

def time2second_2(time):
	[m, s] = map(int, time.split(':'))
	return m * 60 + s

[n, training_time] = input().split()
n = int(n)
training_time = time2second_1(training_time)

playlist = []
playlistHeap = []

for i in range(n):
	play_time = input()
	play_time = time2second_2(play_time)

	playlist.append(play_time)
	heappush(playlistHeap, (play_time, i))

max_music = 0
start_idx = len(playlist)

while playlistHeap:
	temp_time = training_time
	temp_cnt = 0

	[ music_time, music_idx ] = heappop(playlistHeap)
	temp_idx = music_idx

	while temp_time > 0 and temp_idx < len(playlist):
		temp_time -= playlist[temp_idx]
		temp_idx += 1
		temp_cnt += 1
	
	if max_music < temp_cnt:
		max_music = temp_cnt
		start_idx = music_idx
	elif max_music == temp_cnt and start_idx > music_idx:
		max_music = temp_cnt
		start_idx = music_idx
	
print(f'{max_music} {start_idx + 1}')




""" 2 1
7 00:05:48
02:14
03:34
02:34
03:45
05:43
01:34
02:33
"""

""" 3 1
7 00:05:49
02:14
03:34
02:34
03:45
05:43
01:34
02:33
"""

""" 3 2
7 00:05:48
09:14
01:34
02:34
03:45
05:43
01:34
02:33
"""

"""
4 00:00:01
01:00
01:00
01:00
01:00
"""