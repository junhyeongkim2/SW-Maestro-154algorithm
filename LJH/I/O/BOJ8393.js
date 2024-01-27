const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = fs.readFileSync(filePath).toString();
input = Number(input);
let result = 0;
for (let i = 1; i <= input; i++) {
    result += i;
}
console.log(result);
