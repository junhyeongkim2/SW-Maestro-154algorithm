const fs = require("fs");
let input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .map((item) => +item);

console.log(input[0] + input[1]);
