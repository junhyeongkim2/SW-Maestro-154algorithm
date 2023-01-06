const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = fs.readFileSync(filePath).toString().trim();
input = +input;
const dp = [0, 1, 3];

for (let i = 3; i <= input; i++) {
  dp[i] = dp[i - 1] + dp[i - 2];
  dp[i - 1] = dp[i];
  if (i % 2 === 0) {
    dp[i] = (dp[i] + 2) % 10007;
  }
  if (i % 2 !== 0) {
    dp[i] = (dp[i] + 1) % 10007;
  }
}

console.log(dp[input]);
