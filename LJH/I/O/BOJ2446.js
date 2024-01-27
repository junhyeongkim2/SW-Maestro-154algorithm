const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = Number(fs.readFileSync(filePath).toString());
