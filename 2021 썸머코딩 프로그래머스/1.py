def solution(code, day, data):
	docs = []

	for doc in data:
		price_, code_, time_ = doc.split()
		code_ = code_[5:]
		time_ = time_[5:]
		
		if code == code_ and time_.startswith(day):
			docs.append((code_, time_, price_[6:]))
	
	docs.sort(key=lambda x: x[1])

	return list(map(lambda x: int(x[2]), docs))

# [110, 90]
print(solution("012345", "20190620", [
	"price=80 code=987654 time=2019062113",
	"price=90 code=012345 time=2019062014",
	"price=120 code=987654 time=2019062010",
	"price=110 code=012345 time=2019062009",
	"price=95 code=012345 time=2019062111"
]))