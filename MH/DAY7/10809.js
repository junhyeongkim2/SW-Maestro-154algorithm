const path = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = require("fs").readFileSync(path).toString().trim();

const arr = "abcdefghijklmnopqrstuvwxyz";
const answer = [];
for (let i = 0; i < 26; i++) {
  answer.push(input.indexOf(arr[i]) ?? -1);
}

console.log(answer.join(" "));
