const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((item) => +item);

const [a, b] = input;

console.log(a + b);
