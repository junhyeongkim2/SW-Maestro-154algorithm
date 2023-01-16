const path = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = require('fs').readFileSync(path).toString().trim();

let arr = 'abcdefghijklmnopqrstuvwxyz';
let answer = [];

for(let j=0; j<26; j++){
  answer[j] = input.split(arr[j]).length-1
}

console.log(answer.join(' '))