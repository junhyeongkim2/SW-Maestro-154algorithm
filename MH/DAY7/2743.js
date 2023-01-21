const path = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = require("fs").readFileSync(path).toString().trim();

console.log(input.length)