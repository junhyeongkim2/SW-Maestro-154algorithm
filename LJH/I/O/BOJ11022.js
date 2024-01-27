const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
let t = Number(input[0]);
input.slice(1).forEach((e, i) => {
    let [a, b] = e.split(" ").map(Number);
    console.log(`Case #${i + 1}: ${a} + ${b} = ${a + b}`);
});
