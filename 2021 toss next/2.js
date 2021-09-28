/*
 * 현재 온라인인 보험 전문가의 목록을 반환하도록 함수를 작성해주세요.
 * (반환 타입: Promise<string[]>)
 */
async function solution(fetchExperts, fetchIsExpertOnline) {
	const onlineExpertList = [];
	
	// 보험 전문가의 목록을 반환하는 비동기 함수 (반환 타입: Promise<string[]>)
	const expertList = await fetchExperts();

	// 보험 전문가가 온라인인지 여부를 반환하는 함수 (반환 타입: Promise<boolean>)
	const checkOnlineList = await Promise.all(expertList.map(expert => fetchIsExpertOnline(expert)));
	
	checkOnlineList.forEach((v, idx) => {
		if (v) {
			onlineExpertList.push(expertList[idx]);
		}
	})

	return onlineExpertList;
}


