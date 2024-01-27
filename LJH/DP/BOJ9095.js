const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n").map(Number);
input = input.slice(1);
let dp = {
    1: 1,
    2: 2,
    3: 4,
};
input.forEach((n) => {
    for (let i = 4; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }
    console.log(dp[n]);
});
