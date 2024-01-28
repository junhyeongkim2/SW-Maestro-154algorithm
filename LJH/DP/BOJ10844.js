const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let n = Number(fs.readFileSync(filePath).toString());
let dp = {
    1: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
};
const mod = 10 ** 9;
for (let i = 2; i <= n; i++) {
    dp[i] = Array(10).fill(0);
    for (let j = 0; j <= 9; j++) {
        if (j === 0) dp[i][j] = dp[i - 1][j + 1];
        else if (j === 9) dp[i][j] = dp[i - 1][j - 1];
        else dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1];
        dp[i][j] %= mod;
    }
}

let result = dp[n].reduce((acc, cur) => (acc + cur) % mod);
console.log(result);
