# 해시

def solution(pb):
	for p in pb:
		for i in pb:
			if p != i and i.startswith(p):
				return False
	return True