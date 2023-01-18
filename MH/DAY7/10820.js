const path = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = require("fs").readFileSync(path).toString().split("\n");
let result = '';

for (let i = 0; i < input.length; i++) {
  if (input[i] === "") continue;
  let arr = new Array(4).fill(0);
  input[i] = input[i].replace("\r", "").split("");
  for (let x of input[i]) {
    if (/[a-z]/.test(x)) arr[0]++;
    if (/[A-Z]/.test(x)) arr[1]++;
    if (/[\s]/.test(x)) arr[3]++;
    if (/[0-9]/.test(x)) arr[2]++;
  }
  result += arr.join(' ') + '\n';
}

console.log(result.trim());