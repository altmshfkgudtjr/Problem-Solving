def solution(prices):
	len_prices = len(prices)
	answer = [0 for _ in range(len_prices)]
	profit = set([])
	
	for idx, price in enumerate(prices):
		tmp = set([])
		for target in profit:
			answer[target] += 1
			if prices[target] <= price:
				tmp.add(target)
		profit = tmp
		profit.add(idx)

	return answer

print(solution([1,2,3,2,3]))
# [4,3,1,1,0]


"""
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.


"""