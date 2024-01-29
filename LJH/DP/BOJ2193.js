const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let n = Number(fs.readFileSync(filePath).toString());
let dp = {
    1: 1,
    2: 1,
};
for (let i = 3; i <= n; i++) {
    // Number 의 최대 표현 범위는 2^53 -1(약 10^16~17) 이기 때문에 이를 초과할 시 BigInt 자료형으로 변환해주어야 한다.
    // BigInt는 Number와 연산할 수 없기 때문에 같은 자료형으로 변환해준 뒤 연산한다.
    dp[i] = BigInt(dp[i - 1]) + BigInt(dp[i - 2]);
}
// BigInt를 Number로 바꿔주면 정확성을 잃을 수도 있으니 String으로 변환해주어 출력한다.
console.log(String(dp[n]));
