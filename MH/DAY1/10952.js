const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

for (let i = 0; i < input.length - 1; i++) {
  let output = input[i].split(" ").map((item) => +item);
  console.log(output[0] + output[1]);
}
