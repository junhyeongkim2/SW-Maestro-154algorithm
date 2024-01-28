const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let n = Number(fs.readFileSync(filePath).toString());
let dp = {
    1: 1,
    2: 1,
};
for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
}
console.log(dp[n]);
