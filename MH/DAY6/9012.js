const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
let stack = [];
const T = input.shift();

for (let i = 0; i < T; i++) {
  const arr = input[i].trim().split("");

  for (let j = 0; j < input[i].trim().length; j++) {
    stack.push(arr[j]);
    if (stack.slice(-2).join("") === "()") {
      stack.pop();
      stack.pop();
    }
  }
  console.log(stack.length === 0 ? "YES" : "NO");
  stack = [];
}
