const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = fs.readFileSync(filePath).toString();
input = Number(input);
for (let i = input; i >= 1; i--) {
    process.stdout.write(String(i) + "\n");
}
