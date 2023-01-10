//포도주 시식
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((item) => +item);

let n = input.shift();
const dp = new Array(+n).fill(0);
dp[1] = input[0];
dp[2] = input[0] + input[1];

for (let i = 3; i <= n; i++) {
  dp[i] = dp[i - 3] + input[i - 1] + input[i - 2];
  dp[i] = Math.max(dp[i], dp[i - 2] + input[i - 1]);
  dp[i] = Math.max(dp[i], dp[i - 1]);
}

console.log(dp[n]);
