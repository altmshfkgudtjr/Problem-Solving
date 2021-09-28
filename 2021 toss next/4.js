/** Singleton Store */
// const store = {
// 	isFirst: true,
// 	pendingAPI: [],
// }

const store = {
  token: null,
  pendings: [],
  isRunning: false,
};

async function solution(callAPI) {
  if (store.isRunning) {
    store.pendingAPI.push(callAPI);
    return;
  }
  store.isRunning = true;

  const { result, token } = store.token
    ? await callAPI(store.token)
    : await callAPI();

  store.token = token;
  store.isRunning = false;

  const next = store.pendingAPI.shift();
  if (!!next) solution(next);

  return result;
}

const A = (token) => {
  console.log(token);
  return new Promise((resolve) => {
    setTimeout(() => resolve({ token: "token-A", result: "A" }), 500);
  });
};

const B = (token) => {
  console.log(token);
  return new Promise((resolve) => {
    setTimeout(() => resolve({ token: "token-B", result: "B" }), 1000);
  });
};

const C = (token) => {
  console.log(token);
  return new Promise((resolve) => {
    setTimeout(() => resolve({ token: "token-C", result: "C" }), 1200);
  });
};

const D = (token) => {
  console.log(token);
  return new Promise((resolve) => {
    setTimeout(() => resolve({ token: "token-D", result: "D" }), 800);
  });
};

const E = (token) => {
  console.log(token);
  return new Promise((resolve) => {
    setTimeout(() => resolve({ token: "token-E", result: "E" }), 200);
  });
};

solution(A);
solution(B);
solution(C);
solution(D);
solution(E);

/* ======================================================= */

/* 
TOSS가 보안을 신경쓰기 위해서
이전 API에서 반환한 Token을 다음 API에서 사용하기로 하였다.
ok?

첫번째 API를 제외한 모든 API는 이전 API에서 반환한 token이 있어야한다.


callAPI(token) -> Promise<{ result: object, token: string }>

시간 -> 

A호출   B호출
        |
        ㄴ-------B호출            

                A응답
*/
