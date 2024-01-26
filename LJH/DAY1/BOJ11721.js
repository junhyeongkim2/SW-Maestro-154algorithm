// 문자열은 splice 가 없으므로 slice 또는 substring을 사용해야 한다.
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = fs.readFileSync(filePath).toString();
let inputLen = Math.ceil(input.length / 10);
for (let i = 1; i <= inputLen; i++) {
    console.log(input.slice((i - 1) * 10, i * 10));
}
