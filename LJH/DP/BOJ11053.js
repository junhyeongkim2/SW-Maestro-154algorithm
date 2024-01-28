const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function solution(n, arr) {
    let dp = Array(n + 1).fill(1);
    for (let i = 1; i < n; i++) {
        const values = [1];
        for (let j = i - 1; j >= 0; j--) {
            if (arr[j] < arr[i]) values.push(dp[j] + 1);
        }
        dp[i] = Math.max(...values);
    }
    console.log(Math.max(...dp));
}
let input = [];
rl.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    const n = Number(input[0]);
    const arr = input[1].split(" ").map(Number);
    solution(n, arr);
    process.exit();
});
