const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((i) => +i);
const length = input.shift();
const dp = [0, 1, 2, 4];

input.forEach((item) => {
  for (let i = 4; i <= item; i++) {
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
  }
});

for (let i = 0; i < length; i++) {
  console.log(dp[input[i]]);
}
