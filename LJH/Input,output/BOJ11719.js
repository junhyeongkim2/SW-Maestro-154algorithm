const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
const input = fs.readFileSync(filePath).toString();
console.log(input);
