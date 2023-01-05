const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

for (let i = 0; i < input[0]; i++) {
  let output = input[i + 1].split(" ").map((item) => +item);
  console.log(output[0] + output[1]);
}
