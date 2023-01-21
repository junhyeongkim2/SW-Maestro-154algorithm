const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');
const T = input.shift();

for(let i=0; i<T; i++){
  const sum = input[i].split(',').map(item => +item).reduce((prev,cur)=>prev+cur);
  console.log(sum)
}