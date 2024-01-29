const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = fs.readFileSync(filePath).toString();
input = Number(input);
for (let i = 1; i <= 9; i++) {
    console.log(`${input} * ${i} = ${input * i}`);
}
