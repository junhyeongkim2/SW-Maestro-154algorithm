//메모리 초과가 뜨는데 풀이 과정은 맞은 문제 - 완전탐색 
const path = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = require("fs").readFileSync(path).toString().trim().split(" ");

let x = 1;
while (true) {
  x++;
  if (
    (x - input[0]) % 15 === 0 &&
    (x - input[1]) % 28 === 0 &&
    (x - input[2]) % 19 === 0
  ) {
    console.log(x);
    process.exit();
  }
}
