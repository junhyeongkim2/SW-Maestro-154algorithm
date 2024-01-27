const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
input = input[1].split("").map(Number);
let result = input.reduce((acc, cur) => (acc += cur));
console.log(result);
