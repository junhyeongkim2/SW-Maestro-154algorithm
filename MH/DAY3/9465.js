const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

const T = +input.shift();
const n = input.filter((_, index) => index % 3 === 0);
const dp = new Array(T + 1).fill([]);

for (let i = 0; i < T; i++) {
  dp[0] = new Array(+n[i]).fill(0);
  dp[1] = input[3 * i + 1].split(" ").map((item) => +item);
  dp[2] = input[3 * i + 2].split(" ").map((item) => +item);
  for (let j = 1; j < n[i]; j++) {
    dp[0][j] = Math.max(dp[1][j - 1], dp[2][j - 1]);
    dp[1][j] = Math.max(dp[0][j - 1], dp[2][j - 1]) + dp[1][j];
    dp[2][j] = Math.max(dp[0][j - 1], dp[1][j - 1]) + dp[2][j];
  }
  console.log(Math.max(dp[0][n[i] - 1], dp[1][n[i] - 1], dp[2][n[i] - 1]));
}
