const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let n = Number(fs.readFileSync(filePath).toString());
let dp = {
    1: 9,
};
for (let i = 2; i <= n; i++) {
    dp[i] = i % 2 === 0 ? (dp[i - 1] * 2 - 1) % 10 ** 9 : (dp[i - 1] * 2 - 2) % 10 ** 9;
}
console.log(dp[n]);
