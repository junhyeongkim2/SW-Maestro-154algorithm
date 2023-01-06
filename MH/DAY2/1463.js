const fs = require("fs");
let input = fs.readFileSync("../input.txt").toString();
let x = +input;
let arr = [0, 0, 1, 1, 2];

for (let i = 5; i < x + 1; i++) {
  let one = Number.MAX_SAFE_INTEGER;
  let two = Number.MAX_SAFE_INTEGER;
  let three = arr[i - 1];
  if (i % 3 === 0) {
    one = arr[i / 3];
  }
  if (i % 2 === 0) {
    two = arr[i / 2];
  }
  arr.push(1 + Math.min(one, two, three));
}
console.log(arr[x]);
