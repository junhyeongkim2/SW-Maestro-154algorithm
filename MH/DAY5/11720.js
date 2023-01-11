const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');
const T = input.shift();
const arr = input[0].split('').map(item => +item);
let sum = 0;
for(let i=0; i<T; i++){
  sum += arr[i];
}

console.log(sum)