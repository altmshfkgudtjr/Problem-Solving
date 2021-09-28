/*
 * `codeOwnersMap`과 `directory`를 입력받아
 * `directory`의 코드 주인 목록을 반환하는 함수를 작성하세요.
 */
function solution(codeOwnersMap, directory) {
  const folders = directory.split("/");
  let currentDir = codeOwnersMap;

  folders.forEach((folder) => (currentDir = currentDir[folder]));

  return currentDir;
}

/* 코드 주인 정보 예시 */
const codeOwnersMap = {
  scripts: ["배수진"],
  services: {
    "business-ledger": ["고찬균", "배수진"],
    "toss-card": ["채주민", "유재섭"],
    payments: ["유재섭"],
  },
};

/* 예시 실행 결과 */
// ['배수진']
solution(codeOwnersMap, "scripts");

// ['고찬균', '배수진']
solution(codeOwnersMap, "services/business-ledger");

// ['유재섭']
solution(codeOwnersMap, "services/payments");

/* 
	1. 비동기 프로그래밍에 대하여
		- 비동기 프로그래밍란 무엇이라고 생각하시나요?
		- 비동기 프로그래밍을 하는 이유와 어떤 대표적으로 어떻게 사용할 수 있을까요?
		- 비동기 프로그래밍하면서 어려웠었던 경험, 해결방법을 알려주세요
	2. 컴포넌트에 대하여
		- 컴포넌트를 왜 사용하나요?
		- 컴포넌트를 작성하는 것에 당신만의 원칙이 있나요? 있으면 알려주세요
		- 좋은 컴포넌트란 무엇인가요?
	3. UI 상태관리에 대하여
		- UI 상태관리를 사용해봤던 경험
		- 
*/
