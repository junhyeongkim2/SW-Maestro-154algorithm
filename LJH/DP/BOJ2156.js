const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function solution(input) {
    input = input.map(Number);
    const [n, ...wine] = input;
    wine.unshift(0);
    const dp = Array(n + 1).fill(0);
    dp[1] = wine[1];
    dp[2] = wine[1] + wine[2];
    for (let i = 3; i <= n; i++) {
        //prettier-ignore
        dp[i] = Math.max(
            dp[i-3]+wine[i-1]+wine[i],
            dp[i-2]+wine[i],
            dp[i-1]
        );
    }
    console.log(dp[n]);
}

let input = [];
rl.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    solution(input);
    process.exit();
});
