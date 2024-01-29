const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = Number(fs.readFileSync(filePath).toString());
for (let i = 1; i <= input; i++) {
    for (let j = input; j >= i; j--) {
        process.stdout.write("*");
    }
    console.log();
}
