const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let n = Number(fs.readFileSync(filePath).toString());
for (let i = 1; i <= n; i++) {
    // 첫 줄일 경우 n-1번 띄어쓰기 후 별표(*) 한 개 출력
    if (i === 1) {
        for (let j = 0; j < n - i; j++) process.stdout.write(" ");
        process.stdout.write("*");
    }
    // 마지막 줄일 경우 2*n-1번 별표(*) 출력
    else if (i === n) {
        process.stdout.write("*".repeat(2 * n - 1));
    }
    // 첫 번째 줄도 마지막 줄도 아닐 경우
    // 1. n-i번 띄어쓰기 후 별표(*) 한 개 출력
    // 2. 2*i-3 번 띄어쓰기 후 별표(*) 한 개 출력
    else {
        for (let j = 1; j <= n - i; j++) process.stdout.write(" ");
        process.stdout.write("*");
        for (let j = 1; j <= 2 * i - 3; j++) process.stdout.write(" ");
        process.stdout.write("*");
    }
    console.log();
}
