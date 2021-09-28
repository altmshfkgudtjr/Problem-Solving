function parseSearch(search) {
	const parsed = {};

	/* 쿼리 문자열 `search`를 파싱하는 함수를 작성해주세요. */
	const querySetList = search.startsWith('?')
		? search.slice(1).split('&')
		: [];

	querySetList.forEach(query => {
		const [key, value] = query.split('=');
		if (parsed[key]) {
			if (typeof parsed[key] === 'string') {
				parsed[key] = [ parsed[key], value ];
			} else {
				parsed[key] = [ ...parsed[key], value ];
			}
		} else {
			parsed[key] = value;
		}
	});

	return parsed;
}

/*
* NOTE: 아래 코드는 코드 동작을 확인하기 위한 코드입니다. 수정하지 말아주세요.
*/
function solution(search) {
	var query = parseSearch(search);
	return submit(query);
}

function submit(answer) {
	return JSON.stringify(answer);
}

console.log(parseSearch(""))
console.log(parseSearch("?from=twitter"))
console.log(parseSearch("?range=1&range=8"))
console.log(parseSearch("?from=main"))
console.log(parseSearch("?from=facebook&from=ad"))
console.log(parseSearch("?from=facebook&from=article"))