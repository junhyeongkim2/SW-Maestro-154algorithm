const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let n = Number(fs.readFileSync(filePath).toString());
const mod = 10007;
let dp = {
    1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
};
for (let i = 2; i <= n; i++) {
    dp[i] = Array(10).fill(0);
    for (let j = 0; j <= 9; j++) {
        for (let k = j; k <= 9; k++) {
            dp[i][j] += dp[i - 1][k];
            dp[i][j] %= mod;
        }
    }
}
result = dp[n].reduce((acc, cur) => (acc + cur) % mod);
console.log(result);
