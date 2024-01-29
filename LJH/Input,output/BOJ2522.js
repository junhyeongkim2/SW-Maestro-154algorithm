const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = Number(fs.readFileSync(filePath).toString());
for (let i = 1; i <= input; i++) {
    for (let j = 1; j <= input - i; j++) process.stdout.write(" ");
    for (let j = 1; j <= i; j++) process.stdout.write("*");
    console.log();
}
for (let i = 1; i <= input - 1; i++) {
    for (let j = 1; j <= i; j++) process.stdout.write(" ");
    for (let j = 1; j <= input - i; j++) process.stdout.write("*");
    console.log();
}
