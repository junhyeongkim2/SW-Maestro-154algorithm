const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = Number(fs.readFileSync(filePath).toString());
for (let i = 0; i < input; i++) {
    for (let j = 0; j <= i; j++) {
        process.stdout.write("*");
    }
    process.stdout.write("\n");
}
