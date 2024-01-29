// O(NlogN) 으로 풀어야 함
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
let t = Number(input.shift());
while (t--) {
    let col = Number(input.shift());
    let tRow = input.shift().split(" ").map(Number);
    let bRow = input.shift().split(" ").map(Number);
    let dp = [[0, tRow[0], bRow[0]]]; // [이전 열의 최대값, (이전 열 아래 행에 있는 값 + 현재 열 윗 행에 있는 값), (이전 열 윗 행에 있는 값 + 현재 열 아래 행에 있는 값)]
    for (let i = 1; i <= col; i++) {
        dp[i] = [
            Math.max(...dp[i - 1]), // 이전 열에서 아무것도 수행하지 않은 경우, 현재 열에서 위/아래 아무곳이나 선택 가능하므로 현재 열에서 값이 큰 행을 선택
            Math.max(dp[i - 1][0], dp[i - 1][2]) + tRow[i], // max(이전 열에서 아무것도 수행하지 않은 경우, 이전 열에서 아래 행을 골랐을 경우) + 현재 열의 위의 행
            Math.max(dp[i - 1][0], dp[i - 1][1]) + bRow[i], // max(이전 열에서 아무것도 수행하지 않은 경우, 이전 열에서 위의 행을 골랐을 경우) + 현재 열의 아래 행
        ];
    }
    console.log(Math.max(...dp[col - 1]));
}
