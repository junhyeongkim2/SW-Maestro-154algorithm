const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
input.forEach((e) => {
    let [a, b] = e.split(" ").map(Number);
    if (a || b) console.log(a + b);
});
