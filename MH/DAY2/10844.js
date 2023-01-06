const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = fs.readFileSync(filePath).toString().trim();
input = +input;
const memo = new Array(input);
for (let i = 0; i < memo.length; i++) {
  memo[i] = new Array(10).fill(0);
}
memo[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1];

for (let i = 1; i < input; i++) {
  memo[i][0] = memo[i - 1][1] % 1000000000;
  memo[i][9] = memo[i - 1][8] % 1000000000;
  for (let j = 1; j < 9; j++) {
    memo[i][j] = (memo[i - 1][j - 1] + memo[i - 1][j + 1]) % 1000000000;
  }
}

let count = 0;
for (let i = 0; i < 10; i++) {
  count += memo[input - 1][i];
}

console.log(count % 1000000000);
