const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = fs.readFileSync(filePath).toString().trim();
input = +input;
const dp = new Array(input).fill([]);
for (let x = 0; x < input; x++) {
  dp[x] = new Array(10).fill(1);
}

for (let i = 1; i < input; i++) {
  dp[i][0] = 1 % 10007;
  for (let j = 1; j <= 9; j++) {
    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 10007;
  }
}

const answer = dp[input - 1];
const sum = answer.reduce((prev, cur) => prev + cur);
console.log(sum % 10007);
